from pytube import YouTube

from pytube import Playlist

import os

import moviepy.editor as mp

import re

print("Enter URL of YouTube Playlist: ")

url = input()

playlist = Playlist(url)

for u in playlist:
    print(u)

for vid in playlist.videos:
    print(vid)