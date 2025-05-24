import yt_dlp

def download_audio(link:str) -> None:
  ydl_opts = {
    'extract_audio': True,
    'format': 'bestaudio/best[height<=1080]',
    'outtmpl': 'downloads/%(title)s.mp3'
  }
  with yt_dlp.YoutubeDL(ydl_opts) as video:
    info_dict = video.extract_info(link, download = True)
    video_title = info_dict['title']
    print(video_title)
    video.download(link)

def download_channel_audio(channel_link:str) -> None:
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

  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([channel_link])

def download_audio_queue(download_queue_list:list[str]) -> None:
  for video in download_queue_list:
    download_audio(video)

def download_playlist_audio(playlist_link:str) -> None:
  ydl_opts = {
    'extract_audio': True,
    'format': 'bestaudio/best[height<=1080]',
    'outtmpl': 'downloads/%(playlist)s/%(playlist_index)s - %(title)s.mp3',
  }
  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_link])