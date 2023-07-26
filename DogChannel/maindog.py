import os
from youtube_uploader_selenium import YouTubeUploader
import csv


import subprocess
subprocess.call([r'pydown.bat'])
subprocess.call([r'maintiktok.bat'])
number = 11
#Processing the first shit

with open(r'links_file.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    title = list(csv_reader)

from tiktokscraper import tiktokScraper
p1 = tiktokScraper('https://www.tiktok.com/tag/dog?lang=en')
p1.databot()

#Upload shit
for i in range(8):
    video_path = r""+str(i)+"tiktok.mp4"
    metadata_path = r'rockets_metadata0.json'
    uploader = YouTubeUploader(video_path, metadata_path)
    was_video_uploaded = uploader.upload()
    assert was_video_uploaded



