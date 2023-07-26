from pytube import YouTube
import os
import csv
# where to save
SAVE_PATH = "E:/"  # to_do
import subprocess
subprocess.call([r'C:\Users\Death\Desktop\Main Uploader\DogChannel\geturl.bat'])

# link of the video to be downloaded
# opening the file
link = open(r'C:\Users\Death\Desktop\Main Uploader\DogChannel\links_file.csv', 'r')
with open(r'C:\Users\Death\Desktop\Main Uploader\DogChannel\links_file.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    link = list(csv_reader)


for i in range(5):
    print(str(link[i]))
    yt = YouTube(str(link[i]))
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(r'C:\Users\Death\Desktop\Main Uploader\DogChannel'):
        os.makedirs(r'C:\Users\Death\Desktop\Main Uploader\DogChannel')
    yt.download(r'C:\Users\Death\Desktop\Main Uploader\DogChannel',filename=str(i)+".mp4")

