from flask import Flask, render_template, request, send_file, redirect, flash, after_this_request
from zipfile import ZipFile
import shutil
import yt_dlp
import tempfile
import os

app = Flask(__name__)
app.secret_key = 'dev'  # Required for flashing messages


def download_with_yt_dlp(link: str, options: dict) -> tempfile.NamedTemporaryFile:
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=options.get('suffix', '.mp4'))

    ydl_opts = {
        'outtmpl': temp_file.name,
        **options
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

    return temp_file


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download_video', methods=['POST'])
def download_video():
    url = request.form['url']
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            ydl_opts = {
                'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]/best',
                'outtmpl': os.path.join(tmpdir, '%(title)s.%(ext)s'),
                'quiet': True,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)

            return send_file(filename, as_attachment=True, download_name=os.path.basename(filename))
    except Exception as e:
        flash(f"Fout bij downloaden van video: {str(e)}")
        return redirect('/')

@app.route('/download_audio', methods=['POST'])
def download_audio():
    url = request.form['url']
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            ydl_opts = {
                'format': 'bestaudio/best',
                'extract_audio': True,
                'audio_format': 'mp3',
                'outtmpl': os.path.join(tmpdir, '%(title)s.%(ext)s'),
                'quiet': True,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)

            return send_file(filename, as_attachment=True, download_name=os.path.basename(filename))
    except Exception as e:
        flash(f"Fout bij downloaden van audio: {str(e)}")
        return redirect('/')


def download_playlist_to_temp(link: str, ydl_opts: dict, suffix: str):
    with tempfile.TemporaryDirectory() as tmpdir:
        ydl_opts['outtmpl'] = os.path.join(tmpdir, '%(title)s.%(ext)s')

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

        # Create a zip file from all downloaded files
        zip_path = os.path.join(tempfile.gettempdir(), f'playlist_download{suffix}')
        shutil.make_archive(zip_path.replace('.zip', ''), 'zip', tmpdir)

        return zip_path


@app.route('/download_playlist_video', methods=['POST'])
def download_playlist_video():
    url = request.form['url']
    try:
        options = {
            'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]/best',
            'noplaylist': False,
            'quiet': True,
            'playlistend': 10  # You can increase this if needed
        }

        zip_path = download_playlist_to_temp(url, options, '.zip')
        return send_file(zip_path, as_attachment=True, download_name="playlist_video.zip")
    except Exception as e:
        flash(f"Fout bij downloaden van playlist (video): {str(e)}")
        return redirect('/')


@app.route('/download_playlist_audio', methods=['POST'])
def download_playlist_audio():
    url = request.form['url']
    try:
        options = {
            'format': 'bestaudio/best',
            'extract_audio': True,
            'audio_format': 'mp3',
            'noplaylist': False,
            'quiet': True,
            'playlistend': 10,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        zip_path = download_playlist_to_temp(url, options, '.zip')

        @after_this_request
        def cleanup(response):
            try:
                os.remove(zip_path)
            except Exception as e:
                print(f"Error cleaning up file: {e}")
            return response

        return send_file(zip_path, as_attachment=True, download_name="playlist_audio.zip")

    except Exception as e:
        flash(f"Fout bij downloaden van playlist (audio): {str(e)}")
        return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
