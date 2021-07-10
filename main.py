from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re

def DowloadPlaylistToMp3(playlist, Location):
    i = 1

    for u in playlist:
        print(f"Downloading Video {i}...")
        fl = YouTube(u).streams.first().download(Location)
        
        print("Converting to mp3...")
        new_file = mp.AudioFileClip(fl)
        flmp3 = fl.replace(fl[len(fl)-1], "3")
        new_file.write_audiofile(flmp3)
        os.remove(fl)

        print(f"Finished Downloading... File saved to {flmp3}")
        i = i + 1

def PlaylistToMp3():
    print("Enter URL of YouTube Playlist: ")
    url = input()

    print("Enter Location to Save Your File: ")
    Location = input()

    print("Analyzing Playlist...")
    playlist = Playlist(url)
    length = len(playlist)
    print(f"Found {length} Videos in Playlist... Downloading {length} Videos...")

    print("Starting Download...")

    DowloadPlaylistToMp3(playlist, Location)

def main():
    PlaylistToMp3()

main()