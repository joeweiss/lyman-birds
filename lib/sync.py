import urllib.request
import os

audio_dir = "/home/we/dust/audio/lyman-birds"

os.makedirs(audio_dir, exist_ok=True)

output = "/home/we/dust/audio/lyman-birds/audio.mp3"
url = "https://xeno-canto.org/sounds/uploaded/OOECIWCSWV/XC718842-LS_59986%20Forest%20Penduline%20Tit%20song%20A.mp3"
urllib.request.urlretrieve(url, output) # First and short way
