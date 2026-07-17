def add_to_queue(download_queue_list:list) -> list:
  link:str = input("video link: ")
  download_queue_list.append(link)
  print("Nieuwe video toegevoegd aan de download queue.")
  return download_queue_list

def list_queue(download_queue_list:list) -> None:
  print(download_queue_list)

def help():
  print("""
   add: voegt een video toe aan de download_queue,
   queue_video: downloadt de queue als video,
   queue_audio: downloadt de queue als audio,
   list: toont de download_queue,
   exit: stopt het programma 
   WAARSCHUWING: de download_queue blijft niet bewaart als je het programma stopt,
   clear: maakt de command line leeg, 
   playlist_video: downloadt een playlist, 
   channel_video: downloadt een youtube kanaal, 
   playlist_audio: downloadt een playlist als audio, 
   channel_audio: downloadt een youtube kanaal als audio, 
   audio: downloadt een video als audio, 
   video: downloadt een video, 
   help: geeft een lijst van alle commands en hun functie. """)