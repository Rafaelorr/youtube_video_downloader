# YouTube Video Downloader

![Python 3.x](https://img.shields.io/badge/python-3.x-blue)
![License: GPL](https://img.shields.io/badge/license-GPL-green)
![Status: Active](https://img.shields.io/badge/status-active-brightgreen)

Een cli Python-tool voor het downloaden van YouTube-video's, playlists en kanalen.

## Functies

- [x] Download YouTube-video's als video (mp4) of audio (mp3)
- [x] Download volledige playlists
- [x] Download alle video's van een kanaal
- [x] Queue-systeem voor meerdere downloads
- [x] Automatische resolutie-aanpassing (standaard 1080p)
- [ ] Configureerbare download-resolutie (in progress)
- [ ] Config-bestand voor standaard instellingen (in progress)
- [ ] CLI-argumenten support (in progress)

## Vereisten

* Python 3.x
* `yt_dlp`

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

Download één publieke video:

```bash
download_video
```

Sluit het script af:

```bash
exit
```

Run de `help` command uit om alle commands te zien.

## Command lijst
| Command | Beschrijving|
| :------ | :---------- |
| add_to_queue | Voegt een link toe aan de download queue |
| download_video_queue | Download de download queue als video |
| download_audio_queue | Download de download queue als audio |
| list_queue | Print alle links in de download queue |
| download_playlist_video | Download alle videos in een playlist als video |
| download_playlist_audio | Download alle videos in een playlist als audio |
| download_channel_video | Download alle videos van een kanaal als video |
| download_channel_audio | Download alle videos van een kanaal als audio |
| download_video | Download een video als video |
| download_audio | Download een video als audio |
| clear | Leegt de command-line |
| exit | Stopt het programma. De download queue wordt niet opgeslagen |
| help | Print alle commands en hun functie |

## Details

De downloadresolutie is 1080p. <br>
Als 1080p geen optie is dan download het programma een resolutie lager.

## Bijdragen

Wil je bijdragen? Voel je vrij om het repo te forken en een pull request of issue te maken.

## Licentie

Dit project is te gebruiken onder de GPL-licentie.

---

## Problemen oplossen

### 403 Forbidden Error

Dit gebeurt vaak wanneer YouTube wijzigingen doorvoert of wanneer de gebruikte versie van `yt_dlp` verouderd is.

**Oplossing: update `yt_dlp` naar de nieuwste versie**

```bash
pip install -U yt_dlp
```

Alternatief (als `pip` faalt):

```bash
python3 -m pip install -U yt_dlp
```

---

### `Unsupported URL` of `Unable to extract` Errors

Deze fouten ontstaan meestal door veranderingen in de structuur van YouTube-links.

**Oplossing:**

1. Update `yt_dlp` (zie hierboven).
2. Controleer of je de juiste link gebruikt (bijvoorbeeld géén playlist-link bij `download_video`).

---

### `HTTP Error 429: Too Many Requests`

YouTube throttlet tijdelijk jouw IP.

**Oplossing:**

* Wacht enkele minuten of gebruik een VPN.
* Download in kleinere batches.

---

### Algemene tips bij fouten

* Update altijd eerst `yt_dlp` bij problemen.
* Gebruik Python 3.x.
* Zorg voor een stabiele internetverbinding.
* Start het script vanuit een terminal met voldoende rechten (bijv. `sudo` op Linux/macOS).

---

Kom je er niet uit? Meld het probleem via de [Issues-pagina](https://github.com/Rafaelorr/youtube_video_downloader/issues).
