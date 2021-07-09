from pytube import YouTube

from pytube import Playlist

import os

import moviepy.editor as mp

import re

print("Enter URL of YouTube Playlist: ")

url = input()

print("Enter Location to Save Your File: ")

Location = input()

playlist = Playlist(url)

u = "https://www.youtube.com/watch?v=iCSCF5oLrJ0"

YouTube(u).streams.first().download(Location)

#for u in playlist:
#    print(u)

for vid in playlist.videos:
    print(vid)