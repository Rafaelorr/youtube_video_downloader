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