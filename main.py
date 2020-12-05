from pytube import YouTube
from moviepy.editor import *
url = input("Enter the URL : ")
yt = YouTube(url)
video = yt.streams.first()
#video.download()
mp4 = VideoFileClip(video)
audio = mp4.audio
audio.write_audiofile(yt.title.mp3)
print("Download Complete !")