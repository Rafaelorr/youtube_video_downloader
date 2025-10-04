import yt_dlp

def download_channel_video(channel_link: str) -> None:
  ydl_opts = {
    'ignoreerrors': True,
    'extract_flat': False,
    'playlistend': None,
    'outtmpl': 'downloads/%(title)s.%(ext)s',
    'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
    'noplaylist': False,
    'playliststart': 1,
  }

  try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      ydl.download([channel_link])
  except yt_dlp.utils.DownloadError as e:
    print(f"[FOUT] DownloadError bij kanaal: {e}")
  except Exception as e:
    print(f"[FOUT] Onverwachte fout bij kanaal: {e}")

def download_playlist_video(playlist_link: str, toon_playlist_index : bool = True) -> None:
  if toon_playlist_index:
    ydl_opts = {
      'ignoreerrors': True,
      'outtmpl': 'downloads/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s',
      'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
    }
  ydl_opts = {
    'ignoreerrors': True,
    'outtmpl': 'downloads/%(playlist)s/%(title)s.%(ext)s',
    'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
  }

  try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      ydl.download([playlist_link])
  except yt_dlp.utils.DownloadError as e:
    print(f"[FOUT] DownloadError bij afspeellijst: {e}")
  except Exception as e:
    print(f"[FOUT] Onverwachte fout bij afspeellijst: {e}")

def download_video(link: str, toon_playlist_index : bool = True) -> None:
  if toon_playlist_index:
    ydl_opts = {
      'ignoreerrors': True,
      'outtmpl': 'downloads/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s',
      'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
    }
  ydl_opts = {
    'ignoreerrors': True,
    'outtmpl': 'downloads/%(playlist)s/%(title)s.%(ext)s',
    'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
  }

  try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      ydl.download([link])
  except yt_dlp.utils.DownloadError as e:
    print(f"[FOUT] DownloadError bij video: {link}")
  except Exception as e:
    print(f"[FOUT] Onverwachte fout bij video: {link} → {e}")

def download_video_queue(download_queue_list: list[str]) -> None:
  for video in download_queue_list:
    print(f"[INFO] Downloaden: {video}")
    download_video(video, toon_playlist_index=False)
