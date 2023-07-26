import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common
import time
import easygui
import csv

if __name__ == '__main__':
    options = uc.ChromeOptions()
    uc = uc.Chrome(options=options)
    uc.get("https://www.tiktok.com/@your_daily_twitch_upload")
    videoname = (uc.find_elements(By.CLASS_NAME, "tiktok-yz6ijl-DivWrapper.e1cg0wnj1")[0]).get_attribute('a')
    print(videoname)
