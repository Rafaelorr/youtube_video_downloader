from pytube import YouTube, Playlist, Channel
import os

def download_channel(channel_link:str) -> None:
  channel = Channel(channel_link)
  for url in channel.video_urls[:3]:
    download_video(url)

def download_playlist(playlist_link:str) -> None:
  playlist = Playlist(playlist_link)
  for url in playlist.video_urls[:3]:
    download_video(url)

def download_video(link:str) -> None:
  yt:YouTube = YouTube(link)
  video = yt.streams.get_lowest_resolution()
    
  video.download()

def add_to_queue(download_queue_list:list) -> list:
  link:str = input("video link: ")
  download_queue_list.append(link)
  print("nieuwe video toegevoegd aan download_queue_list")
  return download_queue_list

def list_queue(download_queue_list:list) -> None:
  print(download_queue_list)

def download_queue(download_queue_list:list) -> None:
  len_queue:int = len(download_queue_list)
  for i in range(len_queue):
    link:str = download_queue_list[i]
    download_video(link=link)

def help():
  print("""
   add_to_queue: voegt video toe aan de download_queue
   download_queue: download de queue,
   list_queue: toont de queue als een python list,
   exit: om het programma te stoppen WAARSCHUWING je download_queue blijf niet bewaart als je het programma stop,
   clear: maak de command line leeg,
   download_playlist: download een volledige playlist,
   download_channel: download een volledig youtube kanaal,
   help: lijst van alle commands en hun functie.
  """) 

download_queue_list:list = []

# user command loop
while True:
  command:str = input("command: ")
  if command == "add_to_queue":
    add_to_queue(download_queue_list=download_queue_list)
  elif command == "download_queue":
    download_queue(download_queue_list=download_queue_list)
  elif command == "exit":
    want_exit:str = input("wil je echt stoppen? y/n ")
    while not want_exit == "y" and not want_exit == "n":
      print("foute input")
      want_exit:str = input("wil je echt stoppen ? y/n ")
    if want_exit == "y":
      exit()
    continue
  elif command == "list_queue":
    list_queue(download_queue_list=download_queue_list)
  elif command == "download_playlist":
    playlist_link :str = input("playlist link: ")
    download_playlist(playlist_link)
  elif command == "download_channel":
    channel_link :str = input("channel link: ")
    download_channel(channel_link)
  elif command == "clear":
    os.system('cls' if os.name == 'nt' else 'clear')
  else:
    help()
