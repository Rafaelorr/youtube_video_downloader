from audio_functies import download_audio, download_channel_audio, download_audio_queue, download_playlist_audio
from video_functies import download_video, download_video_queue, download_channel_video, download_playlist_video
from main_functies import add_to_queue, list_queue, help
import os

download_queue_list:list = []

print("Type 'help' voor een lijst commands")

# user command loop
while True:
  command:str = input(": ")

  if command == "add_to_queue":
    add_to_queue(download_queue_list)

  elif command == "download_video_queue":
    download_video_queue(download_queue_list)
  
  elif command == "download_audio_queue":
    download_audio_queue(download_queue_list)

  elif command == "download_audio":
    link :str = input("Video link: ")
    download_audio(link)
  
  elif command == "download_video":
    link :str = input("Video link: ")
    download_video(link)

  elif command == "exit":
    want_exit:str = input("Wil je echt stoppen? y/n ")
    while not want_exit == "y" and not want_exit == "n":
      print("Foute input")
      want_exit:str = input("Wil je echt stoppen? y/n ")
    if want_exit == "y":
      exit()
    continue
  elif command == "list_queue":
    list_queue(download_queue_list=download_queue_list)

  elif command == "download_playlist_video":
    playlist_link :str = input("Playlist link: ")
    toon_playlist_index :bool = bool(input("Wil je de playlist index toe voegen aan de bestandnamen? (enter = neen): "))
    download_playlist_video(playlist_link, toon_playlist_index=toon_playlist_index)

  elif command == "download_channel_video":
    channel_link :str = input("Kanaal link: ")
    download_channel_video(channel_link)

  elif command == "download_playlist_audio":
    playlist_link :str = input("Playlist link: ")
    toon_playlist_index :bool = bool(input("Wil je de playlist index toe voegen aan de bestandnamen? (enter = neen): "))
    download_playlist_audio(playlist_link, toon_playlist_index=toon_playlist_index)

  elif command == "download_channel_audio":
    channel_link :str = input("Kanaal link: ")
    download_channel_audio(channel_link)

  elif command == "clear":
    os.system('cls' if os.name == 'nt' else 'clear')
  else:
    help()
