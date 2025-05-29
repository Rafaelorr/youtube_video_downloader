import yt_dlp

def download_channel_video(channel_link:str) -> None:

  ydl_opts = {
    'ignoreerrors': True,
    'extract_flat': False,
    'playlistend': None,
    'outtmpl': 'downloads/%(title)s.%(ext)s',
    'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
    'noplaylist': False,
    'playliststart': 1,
  }

  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    try:
      ydl.download([channel_link])
    except yt_dlp.utils.DownloadError:
      print("Niet beschikbaar")

def download_playlist_video(playlist_link:str) -> None:
  ydl_opts = {
    'outtmpl': 'downloads/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s',
    'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
  }
  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    try:
      ydl.download([playlist_link])
    except yt_dlp.utils.DownloadError:
      print("Niet beschikbaar")


def download_video(link:str) -> None:
  ydl_opts = {'outtmpl': 'downloads/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s',
              'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]'}
  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    try:
      ydl.download([link])
    except yt_dlp.utils.DownloadError:
      print("Niet beschikbaar")

def download_video_queue(download_queue_list:list[str]) -> None:
  for video in download_queue_list:
    download_video(video)