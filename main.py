from pytube import YouTube
from moviepy.editor import *
url = input("Enter the URL : ")
yt = YouTube(url)
video = yt.streams.first()
#video.download()
mp4 = VideoFileClip(video)
mp4.audio.write_audiofile(yt.title)
print("Download Complete !")