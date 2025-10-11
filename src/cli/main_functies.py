def add_to_queue(download_queue_list:list) -> list:
  link:str = input("Video link: ")
  download_queue_list.append(link)
  print("Nieuwe video toegevoegd aan de download queue.")
  return download_queue_list

def list_queue(download_queue_list:list) -> None:
  print(download_queue_list)

def help():
  print("""
   add_to_queue: voegt een video toe aan de download_queue,
   download_video_queue: downloadt de queue,
   download_audio_queue: downloadt de queue als audio,
   list_queue: toont de download_queue,
   exit: stopt het programma 
   WAARSCHUWING: de download_queue blijft niet bewaart als je het programma stopt,
   clear: maakt de command line leeg, 
   download_playlist_video: downloadt een playlist, 
   download_channel_video: downloadt een youtube kanaal, 
   download_playlist_audio: downloadt een playlist als audio, 
   download_channel_audio: downloadt een youtube kanaal als audio, 
   download_audio: downloadt een video als audio, 
   download_video: downloadt een video, 
   help: geeft een lijst van alle commands en hun functie. """) 