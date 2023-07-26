import os
from youtube_uploader_selenium import YouTubeUploader
import csv
import subprocess


#Twitch Channels
subprocess.call([r'C:\Users\Death\Desktop\Main Uploader\TwitchDownloader\twitch.bat'])
subprocess.call([r'C:\Users\Death\Desktop\Main Uploader\TwitchDownloader\maintiktok.bat'])
for i in range(8):
    os.system('ffmpeg -i '+str(i)+'.mp4 -vf scale=1080:1920,setdar=1:1 temp'+str(i)+'.mp4')

#Upload shit
for i in range(8):
    video_path = r"C:\Users\Death\Desktop\Main Uploader\TwitchDownloader/temp"+str(i)+".mp4"
    metadata_path = r'C:\Users\Death\Desktop\Main Uploader\TwitchDownloader/rockets_metadata0.json'
    uploader = YouTubeUploader(video_path, metadata_path)
    was_video_uploaded = uploader.upload()
    assert was_video_uploaded



