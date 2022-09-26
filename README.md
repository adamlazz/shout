# Shout

## About this project

It is necessary to hear the Buffalo Bills fight song after they score points. This automates that process using a Chromecast so you can focus on your gameday experience.

Hey-ayyyyyyy-ayyyyyyyy-ayy!

## Setup instructions

1. Clone this repository `git clone git@github.com:adamlazz/shout.git && cd shout`
1. Run `./setup.sh` to install dependencies and download the Shout song. The script will also start a local HTTP server necessary for your Chromecast to stream the Shout song.
1. Modify the `cast_name` and `sleep_time` variables in `shout.py` if necessary.
1. In another terminal window, run `shout.py` to wait for the Bills to score.
1. Get the name of your Chromecast device (preferably an audio device so you can keep the game on while the song plays).
1. Set your Chromecast device to full volume.
1. Wait for the Bills to score.
1. Celebrate!

## Dependencies

* [pychromecast](https://github.com/home-assistant-libs/pychromecast)
