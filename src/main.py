from audio_functies import download_audio,download_channel_audio,download_audio_queue,download_playlist_audio
from video_functies import download_video, download_video_queue, download_channel_video, download_playlist_video
import os


def add_to_queue(download_queue_list:list) -> list:
  link:str = input("video link: ")
  download_queue_list.append(link)
  print("nieuwe video toegevoegd aan download_queue_list")
  return download_queue_list

def list_queue(download_queue_list:list) -> None:
  print(download_queue_list)

def help():
  print("""
   add_to_queue: voegt video toe aan de download_queue,
   download_video_queue: download de queue als video,
   download_audio_queue: download de queue als audio,
   list_queue: toont de queue als een python list,
   exit: om het programma te stoppen 
   WAARSCHUWING je download_queue blijf niet bewaart als je het programma stop,
   clear: maak de command line leeg, 
   download_playlist_video: download een volledige playlist, 
   download_channel_video: download een volledig youtube kanaal als videos, 
   download_playlist_audio: download een volledige playlist als audio, 
   download_channel_audio: download een volledig youtube kanaal als audio, 
   download_audio: download een video als audio, 
   download_video: download een video als video, 
   help: lijst van alle commands en hun functie. 
  """) 

download_queue_list:list = []

print("Typ help voor een lijst van de commands")

# user command loop
while True:
  command:str = input("command: ")

  if command == "add_to_queue":
    add_to_queue(download_queue_list)

  elif command == "download_video_queue":
    download_video_queue(download_queue_list)
  
  elif command == "download_audio_queue":
    download_audio_queue(download_queue_list)

  elif command == "download_audio":
    link :str = input("video link: ")
    download_audio(link)
  
  elif command == "download_video":
    link :str = input("video link: ")
    download_video(link)

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

  elif command == "download_playlist_video":
    playlist_link :str = input("playlist link: ")
    download_playlist_video(playlist_link)

  elif command == "download_channel_video":
    channel_link :str = input("channel link: ")
    download_channel_video(channel_link)

  elif command == "download_playlist_audio":
    playlist_link :str = input("playlist link: ")
    download_playlist_audio(playlist_link)

  elif command == "download_channel_audio":
    channel_link :str = input("channel link: ")
    download_channel_audio(channel_link)

  elif command == "clear":
    os.system('cls' if os.name == 'nt' else 'clear')
  else:
    help()
