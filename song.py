import os
from pytube import YouTube

def dlSong():
    while True:
        try:
            link = str(input('Enter the url of the video: '))

            youtube = YouTube(link)

            audio = youtube.streams.filter(only_audio=True)

            audio_first = audio.first()

            audio_first.download()
            
        except:
            print('An error occurred while downloading the video. Please try again.')
