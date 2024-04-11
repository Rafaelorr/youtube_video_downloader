from pytube import YouTube

def download_video(link:str,opitie:str):
  yt = YouTube(link)
  if opitie == 'highest_resolution':
      video = yt.streams.get_highest_resolution()
  elif opitie == 'audio_only':
    video = yt.streams.get_audio_only()
  elif opitie == 'lowest_resolution':
      video = yt.streams.get_lowest_resolution()
  else:
      print('')
  video.download()