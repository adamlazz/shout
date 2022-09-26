#!/usr/bin/python3

import requests
import time
import datetime
import socket

import pychromecast

cast_name = "Family Room speaker" # Name of Chromecast device
sleep_time = 60 # How often to check for new scores (seconds)

file_name = "shout.mp3"
score_site = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"

def get_current_score(score_site):
	r = requests.get(score_site)

	events = r.json()['events']
	for e in events:
		if "BUF" in e['shortName']:
			game = e['competitions'][0]
			for c in game['competitors']:
				if "BUF" in c['team']['abbreviation']:
					return int(c['score'])

score = get_current_score(score_site)
current_score = score

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local_ip = s.getsockname()[0]
s.close()

while (True):
	current_score = get_current_score(score_site)

	if current_score == 0: # New game
		score = 0

	print(datetime.datetime.now())
	print('Last score:             ' + str(score).rjust(2))
	print('Current score:          ' + str(current_score).rjust(2))
	print('--------------------------')

	if (current_score > score):
		score = current_score

		# Discover and connect to chromecast with configured name
		services, browser = pychromecast.discovery.discover_chromecasts()
		chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[cast_name])

		# Start worker thread and wait for cast device to be ready
		cast = chromecasts[0]
		cast.wait()

		# Play song
		mc = cast.media_controller
		mc.play_media('http://' + local_ip + ':8000/' + file_name, 'audio/mp3')
		mc.block_until_active()
		pychromecast.discovery.stop_discovery(browser)
	elif current_score < score: # Taking points off the board after review?
		score = current_score

	time.sleep(sleep_time)
