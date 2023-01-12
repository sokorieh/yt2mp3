import playlist
from song import dlSong

from pytube import YouTube, Playlist
from art import *

def greet():
    tprint("yt2mp3")
    print ('-' * 44)
    print()

def menu():
    print('[1] for a playlist download.')
    print('[2] for an audio download from a video.')
    print('[3] to exit the program.')

def getInput():
    while True:
        ask = int(input('Enter either 1, 2, or 3: '))

        if ask == 1 or ask == 2:
            return ask
        elif ask == 3:
            break

greet()
menu()
method = getInput()

if method == 2:
    dlSong()