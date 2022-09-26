#!/bin/bash

set -e

shout_song="https://www.youtube.com/watch?v=1JpeDWbgUO8"

cd "$(dirname "$0")"

pip install -r requirements.txt

if ! command -v youtube-dl >/dev/null 2>&1 ; then
	read -p "Press enter to install youtube-dl..."

	sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
	sudo chmod a+rx /usr/local/bin/youtube-dl
fi

if ! command -v ffmpeg >/dev/null 2>&1 ; then
	read -p "Press enter to install ffmpeg..."

	sudo apt-get install -y ffmpeg
fi

if [ ! -f "shout.mp3" ]; then
	youtube-dl --extract-audio --audio-format mp3 --output "shout.mp3" "${shout_song}"
fi

python3 -m http.server

exit 0
