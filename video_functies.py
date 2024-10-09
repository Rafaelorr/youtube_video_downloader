from pytubefix import YouTube, Playlist, Channel

def download_channel_video(channel_link:str) -> None:
  channel = Channel(channel_link)

  for url in channel.video_urls:
    download_video(url)
  print("De download is klaar")

def download_playlist_video(playlist_link:str) -> None:
  playlist = Playlist(playlist_link)

  for url in playlist.video_urls:
    download_video(url)
  print("De download is klaar")

def download_video(link:str) -> None:
  yt:YouTube = YouTube(link)
  video = yt.streams.get_lowest_resolution()

  video.download()

def download_video_queue(download_queue_list:list) -> None:
  len_queue:int = len(download_queue_list)
  for i in range(len_queue):
    link:str = download_queue_list[i]
    download_video(link=link)
  print("De download is klaar")