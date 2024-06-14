from pytube import YouTube

def download_video(link:str,opitie:str,file_extension:str) -> None:
  yt:YouTube = YouTube(link)
  if opitie == 'highest_resolution':
    video = yt.streams.get_highest_resolution()
  elif opitie == 'audio_only':
    video = yt.streams.get_audio_only()
  elif opitie == 'lowest_resolution':
    video = yt.streams.get_lowest_resolution()
  else:
    print('')
  video.download(file_extension=file_extension)

def add_to_queue(download_queue_list:list) -> list:
  link:str = input("video link: ")
  opitie:str = input("opitie highest_resolution, audio_only of lowest_resolution: ")
  file_extension:str = input("video file extension: ")
  download_queue_list.append(link)
  download_queue_list.append(opitie)
  download_queue_list.append(file_extension)
  print("nieuwe video toegevoegd aan download_queue_list")
  return download_queue_list

def list_queue(download_queue_list:list) -> None:
  for item in download_queue_list:
    if download_queue_list.index(item) % 4 == 0 or download_queue_list.index(item) == 0:
      print("video link: ",item)
      continue
    if download_queue_list.index(item) % 2 == 0:
      print("video download opitie: ", item)
      continue
    if download_queue_list.index(item) % 3 == 0:
      print("video file extension: ", item)
      continue

def download_queue(download_queue_list:list) -> None:
  # ! loop bug video info loop niet volledig
  for i in range(len(download_queue_list/3)):
    link:str = download_queue_list[i]
    opitie:str = download_queue_list[i+1]
    file_extension:str = download_queue_list[i+2]
    download_video(link=link,opitie=opitie,file_extension=file_extension)

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
      want_exit:str = input("xil je echt stoppen ? y/n ")
    if want_exit == "y":
      exit()
    continue
  elif command == "list_queue":
    list_queue(download_queue_list=download_queue_list)
  else:
    # help
    print("""
      add_to_queue: lorem
      download_queue: lorem,
      list_queue: lorem,
      exit: lorem,
      help: lorem
    """)
