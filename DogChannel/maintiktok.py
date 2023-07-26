from TiktokBot import TiktokBot
from Cookies import Cookies


for i in range(5):
    if __name__ == "__main__":
        tiktok_bot = TiktokBot()  # "VideosDirPath", is the default directory where images edited will be saved.
        tiktok_bot.upload.directUpload(r"C:\Users\Death\Desktop\Main Uploader\DogChannel/"+str(i)+".mp4")

