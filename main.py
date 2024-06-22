from pytube import YouTube
import os

def download_video(link:str, opitie:str) -> None:
    yt:YouTube = YouTube(link)
    
    if opitie == 'highest_resolution':
        video = yt.streams.get_highest_resolution()
    elif opitie == 'audio_only':
        video = yt.streams.get_audio_only()
    elif opitie == 'lowest_resolution':
        video = yt.streams.get_lowest_resolution()
    else:
        print('')
    
    video.download()

def add_to_queue(download_queue_list:list) -> list:
  link:str = input("video link: ")
  opitie:str = input("opitie highest_resolution, audio_only of lowest_resolution: ")
  download_queue_list.append(link)
  download_queue_list.append(opitie)
  print("nieuwe video toegevoegd aan download_queue_list")
  return download_queue_list

def list_queue(download_queue_list:list) -> None:
  print(download_queue_list)

def download_queue(download_queue_list:list) -> None:
  len_queue:int = len(download_queue_list)
  for i in range(len_queue):
    link:str = download_queue_list[i]
    try:
      opitie:str = download_queue_list[i+1]
    except:
      return
    download_video(link=link,opitie=opitie)
    i + 2

def help():
  print("""
   add_to_queue: voegt video toe aan de download_queue
   download_queue: download de queue,
   list_queue: toont de queue als een python list,
   exit: om het programma te stoppen WAARSCHUWING je download_queue blijf niet bewaart als je het programma stop,
   clear: maak de command line leeg,
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
  elif command == "clear":
    os.system('cls' if os.name == 'nt' else 'clear')
  else:
    help()
