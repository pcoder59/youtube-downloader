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

for u in playlist:
    fl = YouTube(u).streams.first().download(Location)

    new_file = mp.AudioFileClip(fl)

    flmp3 = fl.replace(fl[len(fl)-1], "3")

    new_file.write_audiofile(flmp3)

    os.remove(fl)