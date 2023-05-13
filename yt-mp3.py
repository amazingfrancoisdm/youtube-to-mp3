from pytube import YouTube
import os
  
link = YouTube(str(input("Enter the URL of the video you want to download:")))

video = link.streams.filter(only_audio=True).first()

path = str(input("Enter the output path or press enter for this one:")) or "."

out_video = video.download(output_path=path)

title = str(input("Enter the title you'd like or press enter for default:"))
  
base, ext = os.path.splitext(out_video)

if (len(title)!=0):
    song = title
else:
    song = base

song += ".mp3"

os.replace(out_video, song)
  
print(link.title + " has been successfully downloaded.")

