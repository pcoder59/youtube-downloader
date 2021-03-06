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


def DownloadVideotoMp3(youtube, Location):
    print("Downloading Video...")
    fl = youtube.streams.first().download(Location)

    print("Converting to mp3...")
    new_file = mp.AudioFileClip(fl)
    flmp3 = fl.replace(fl[len(fl)-1], "3")
    new_file.write_audiofile(flmp3)
    os.remove(fl)

    print(f"Finished Downloading... File saved to {flmp3}")

def DownloadVideo(youtube, Location):
    print("Downloading Video...")
    fl = youtube.streams.first().download(Location)
    print(f"Finished Downloading... File saved to {fl}")

def Analyzing(choice):
    print("Enter URL of YouTube Video: ")
    url = input()
    print("Enter Location to Save Your File: ")
    Location = input()

    if choice == 1:
        print("Analyzing Video...")
        youtube = YouTube(url)

        print("Starting Download...")

        DownloadVideo(youtube, Location)

def VideotoMp3():
    print("Enter URL of YouTube Video: ")
    url = input()
    print("Enter Location to Save Your File: ")
    Location = input()

    print("Analyzing Video...")
    youtube = YouTube(url)

    print("Starting Download...")

    DownloadVideotoMp3(youtube, Location)

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
    cont = True
    while(cont):
        print("What Do You Want to Do:")
        print("1. YouTube Video Download")
        print("2. YouTube to mp3")
        print("3. YouTube Playlist to mp3")
        print("4. Exit")
        print("Enter Your Choice: ")
        Choice = int(input())
        if Choice == 1:
            Analyzing(1)
        elif Choice == 2:
            VideotoMp3()
        elif Choice == 3:
            PlaylistToMp3()
        elif Choice == 4:
            cont = False
        else:
            print("Invalid Choice!!! Enter 1, 2, 3 or 4!!!")

main()