from flask import Flask, render_template, request, send_file, redirect, flash
import threading
import yt_dlp
import tempfile
import os
import random
import string

app = Flask(__name__)
app.secret_key = ''.join(random.choices(string.ascii_letters + string.digits, k=10))  # Required for flashing messages


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/download_video', methods=['POST'])
def download_video():
    url = request.form['url']
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            ydl_opts = {
                'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]/best',
                'outtmpl': os.path.join(tmpdir, '%(title)s.%(ext)s'),
                'quiet': True,
                'merge_output_format': 'mp4',  # Ensure the final output is in MP4
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
                    'preferredquality': '190',
                }],
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)

            return send_file(filename, as_attachment=True, download_name=os.path.basename(filename))
    except Exception as e:
        flash(f"Fout bij downloaden van audio: {str(e)}")
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
