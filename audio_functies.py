from pytubefix import YouTube, Playlist, Channel

def download_audio(link:str) -> None:
  yt:YouTube = YouTube(link)
  video = yt.streams.get_audio_only()

  video.download()

def download_channel_audio(channel_link:str) -> None:
  channel = Channel(channel_link)

  for url in channel.video_urls:
    download_audio(url)
  print("De download is klaar")

def download_audio_queue(download_queue_list:list) -> None:
  len_queue:int = len(download_queue_list)
  for i in range(len_queue):
    link:str = download_queue_list[i]
    download_audio(link=link)
  print("De download is klaar")

def download_playlist_audio(playlist_link:str) -> None:
  playlist = Playlist(playlist_link)

  for url in playlist.video_urls:
    download_audio(url)
  print("De download is klaar")