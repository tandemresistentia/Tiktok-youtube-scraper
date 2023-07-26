from pytube import YouTube
import os
import csv
# where to save
SAVE_PATH = "E:/"  # to_do
import subprocess
subprocess.call([r'geturl.bat'])

# link of the video to be downloaded
# opening the file
link = open(r'links_file.csv', 'r')
with open(r'links_file.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    link = list(csv_reader)


for i in range(5):
    print(str(link[i]))
    yt = YouTube(str(link[i]))
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    yt.download(filename=str(i)+".mp4")

