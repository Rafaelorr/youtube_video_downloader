def add_to_queue(download_queue_list:list) -> list:
  link:str = input("video link: ")
  download_queue_list.append(link)
  print("Nieuwe video toegevoegd aan de download queue.")
  return download_queue_list

def list_queue(download_queue_list:list) -> None:
  print(download_queue_list)

def help():
  print("""
    # Download Commands
    ## Download Queue Commands
    * add: voegt een video toe aan de download_queue
    * queue_video: downloadt de queue als video
    * queue_audio: downloadt de queue als audio
    * list: toont de download_queue

    ## Download Enkele Video's
    * video: downloadt een video
    * audio: downloadt een video als audio

    ## Download Playlists
    * playlist_video: downloadt een playlist
    * playlist_audio: downloadt een playlist als audio
    
    ## Download Kanalen
    * channel_video: downloadt een youtube kanaal
    * channel_audio: downloadt een youtube kanaal als audio

        
    # Extra's
    * help: geeft een lijst van alle commands en hun functie
    * clear: maakt de command line leeg
    * exit: stopt het programma
  """)