from pytube import YouTube

def download_video(link:str,opitie:str,file_extension:str):
  yt = YouTube(link)
  if opitie == 'highest_resolution':
      video = yt.streams.get_highest_resolution()
  elif opitie == 'audio_only':
    video = yt.streams.get_audio_only()
  elif opitie == 'lowest_resolution':
      video = yt.streams.get_lowest_resolution()
  else:
      print('')
  video.download(file_extension=file_extension)

def add_to_queue(download_queue:list):
  pass

def list_queue(download_queue:list):
  pass

def download_queue(download_queue:list):
  for i in range(len(download_queue/3)):
    pass