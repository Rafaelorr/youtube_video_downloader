import yt_dlp

def download_channel_video(channel_link:str) -> None:

  ydl_opts = {
    'ignoreerrors': True,
    'extract_flat': False,  # Set to True if you want only metadata without downloading
    'playlistend': None,    # Download all videos
    'outtmpl': 'downloads/%(title)s.%(ext)s',  # Output directory and filename pattern
    'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
    'noplaylist': False, 
    'playliststart': 1,
  }

  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([channel_link])

def download_playlist_video(playlist_link:str) -> None:
  ydl_opts = {
    'outtmpl': 'downloads/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s',
    'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
  }
  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_link])


def download_video(link:str) -> None:
  ydl_opts = {'outtmpl': 'downloads/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s',
              'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]'}
  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

def download_video_queue(download_queue_list:list[str]) -> None:
  for video in download_queue_list:
    download_video(video)