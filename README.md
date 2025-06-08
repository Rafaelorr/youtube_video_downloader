# YouTube Video Downloader

Een cli Python-tool voor het downloaden van YouTube-video's.

## Vereisten
- Python 3.x
- `yt_dlp`

## Installatie

1. Clone de repo:
```bash
git clone https://github.com/Rafaelorr/youtube_video_downloader.git
```

2. Ga naar de directory:
```bash
cd youtube_video_downloader/src/
```

3. Installeer de benodigde dependencies:
```bash
pip install -r requirements.txt
```

## Gebruik

Run het script:

```bash
python3 main.py
```

Run de `help` command uit om alle commands te zien.

## Command lijst

**add_to_queue**: voegt een link toe aan de download queue <br>
**download_video_queue**: download de download queue als video <br>
**download_audio_queue**: download de download queue als audio <br>
**list_queue**: prints alle links in de download queue <br>
**download_playlist_video**: download alle videos in een playlist als video <br>
**download_playlist_audio**: download alle videos in een playlist als audio <br>
**download_channel_video**: download alle videos van een kanaal als video <br>
**download_channel_audio**: download alle videos van een kanaal als audio <br>
**download_video**: download een video als video <br>
**download_audio**: download een video als audio <br>
**clear**: leegt de command-line <br>
**exit**: stopt het programma, PAS OP de download queue wordt geleegt als het programma stopt <br>
**help**: print alle commands en functie

## Details
De download resulotie is 1080p.

Als 1080p geen optie is dan download het programma een resulotie lager.

## Bijdragen
Wil je bijdragen? Voel je vrij om de repo te forken en een pull request in te dienen of issues te melden voor verbeteringen.

## Licentie
Dit project is te gebruiken onder de GPL-licentie.

### to do's
* download resolutie kunnen verandert worden door de gebruiker
* standaard instellingen config
* download direct via cli
