# YouTube Video Downloader

Een cli Python-tool voor het downloaden van YouTube-video's.

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

Run de `help` command uit om alle commands te zien.

## Command lijst

**add\_to\_queue**: voegt een link toe aan de download queue <br>
**download\_video\_queue**: download de download queue als video <br>
**download\_audio\_queue**: download de download queue als audio <br>
**list\_queue**: prints alle links in de download queue <br>
**download\_playlist\_video**: download alle videos in een playlist als video <br>
**download\_playlist\_audio**: download alle videos in een playlist als audio <br>
**download\_channel\_video**: download alle videos van een kanaal als video <br>
**download\_channel\_audio**: download alle videos van een kanaal als audio <br>
**download\_video**: download een video als video <br>
**download\_audio**: download een video als audio <br>
**clear**: leegt de command-line <br>
**exit**: stopt het programma, PAS OP de download queue wordt geleegt als het programma stopt <br>
**help**: print alle commands en functie

## Details

De downloadresolutie is 1080p.

Als 1080p geen optie is dan download het programma een resolutie lager.

## Bijdragen

Wil je bijdragen? Voel je vrij om de repo te forken en een pull request in te dienen of issues te melden voor verbeteringen.

## Licentie

Dit project is te gebruiken onder de GPL-licentie.

## To do's

* download resolutie kunnen veranderd worden door de gebruiker
* standaard instellingen config
* download direct via cli

---

## Problemen oplossen

### ❌ 403 Forbidden Error

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

### ❌ `Unsupported URL` of `Unable to extract` Errors

Deze fouten ontstaan meestal door veranderingen in de structuur van YouTube-links.

**Oplossing:**

1. Update `yt_dlp` (zie hierboven).
2. Controleer of je de juiste link gebruikt (bijvoorbeeld géén playlist-link bij `download_video`).

---

### ❌ `HTTP Error 429: Too Many Requests`

YouTube blokkeert tijdelijk jouw IP vanwege te veel verzoeken.

**Oplossing:**

* Wacht enkele minuten of gebruik een VPN.
* Download in kleinere batches.

---

### ✅ Algemene tips bij fouten

* Update altijd eerst `yt_dlp` bij problemen.
* Gebruik Python 3.x.
* Zorg voor een stabiele internetverbinding.
* Start het script vanuit een terminal met voldoende rechten (bijv. `sudo` op Linux/macOS).

---

Kom je er niet uit? Meld het probleem via de [Issues-pagina](https://github.com/Rafaelorr/youtube_video_downloader/issues).
