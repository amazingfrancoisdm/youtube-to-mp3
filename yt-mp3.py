from pytube import YouTube
import os
  
link = YouTube(str(input("Enter the URL of the video you want to download:")))

video = link.streams.filter(only_audio=True).first()
  
out_video = video.download(output_path=".")
  
base, ext = os.path.splitext(out_video)
song = base + '.mp3'
  
print(link.title + " has been successfully downloaded.")

