import subprocess
subprocess.call([r'C:\Users\Death\Desktop\Main Uploader\DogChannel\pydown.bat'])
subprocess.call([r'C:\Users\Death\Desktop\Main Uploader\DogChannel\z10.bat'])
import os
#Delete
os.remove(r"C:\Users\Death\Desktop\Main Uploader\DogChannel/O.mp4")
dir_name = r"C:\Users\Death\Desktop\Main Uploader\DogChannel/"
test = os.listdir(dir_name)
for item in test:
    if item.endswith(".mp4"):
        os.remove(os.path.join(dir_name, item))

for item in test:
    if item.endswith(".ts"):
        os.remove(os.path.join(dir_name, item))