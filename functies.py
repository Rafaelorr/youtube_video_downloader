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

def add_to_queue(download_queue:list) -> list:
  link:str = input("video link: ")
  opitie:str = input("opitie highest_resolution, audio_only of lowest_resolution: ")
  file_extension:str = input("video file extension: ")
  download_queue.append(link)
  download_queue.append(opitie)
  download_queue.append(file_extension)
  print("nieuwe video toegevoegd aan download_queue")
  return download_queue

def list_queue(download_queue:list) -> None:
  for item in download_queue:
    if download_queue.index(item) % 4 == 0 or download_queue.index(item) == 0:
      print("video link: ",item)
      continue
    if download_queue.index(item) % 2 == 0:
      print("video download opitie: ", item)
      continue
    if download_queue.index(item) % 3 == 0:
      print("video file extension: ", item)
      continue

def download_queue(download_queue:list) -> None:
  for i in range(len(download_queue/3)):
    link:str = download_queue[i]
    opitie:str = download_queue[i+1]
    file_extension:str = download_queue[i+2]
    download_video(link=link,opitie=opitie,file_extension=file_extension)