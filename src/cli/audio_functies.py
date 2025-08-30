import yt_dlp

def download_audio(link: str) -> None:
  ydl_opts = {
    'extract_audio': True,
    'format': 'bestaudio/best[height<=1080]',
    'outtmpl': 'downloads/%(title)s.mp3',
    'ignoreerrors': True,
  }

  try:
    with yt_dlp.YoutubeDL(ydl_opts) as video:
      info_dict = video.extract_info(link, download=True)
      if info_dict:
        print(f"Gedownload: {info_dict['title']}")
      else:
        print(f"Kon info niet ophalen voor: {link}")
  except yt_dlp.utils.DownloadError as e:
    print(f"[FOUT] DownloadError bij audio: {link}")
  except Exception as e:
    print(f"[FOUT] Onverwachte fout bij audio: {link} → {e}")

def download_channel_audio(channel_link: str) -> None:
  ydl_opts = {
    'extract_audio': True,
    'format': 'bestaudio/best[height<=1080]',
    'outtmpl': 'downloads/%(title)s.mp3',
    'ignoreerrors': True,
    'extract_flat': False,
    'playlistend': None,
    'noplaylist': False,
    'playliststart': 1,
  }

  try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      ydl.download([channel_link])
  except yt_dlp.utils.DownloadError as e:
    print(f"[FOUT] DownloadError bij kanaal (audio): {e}")
  except Exception as e:
    print(f"[FOUT] Onverwachte fout bij kanaal (audio): {e}")

def download_audio_queue(download_queue_list: list[str]) -> None:
  for video in download_queue_list:
    print(f"[INFO] Downloaden (audio): {video}")
    download_audio(video)

def download_playlist_audio(playlist_link: str) -> None:
  ydl_opts = {
    'extract_audio': True,
    'format': 'bestaudio/best[height<=1080]',
    'outtmpl': 'downloads/%(playlist)s/%(playlist_index)s - %(title)s.mp3',
    'ignoreerrors': True,
  }

  try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      ydl.download([playlist_link])
  except yt_dlp.utils.DownloadError as e:
    print(f"[FOUT] DownloadError bij afspeellijst (audio): {e}")
  except Exception as e:
    print(f"[FOUT] Onverwachte fout bij afspeellijst (audio): {e}")
