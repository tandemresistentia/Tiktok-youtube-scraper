from Browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common
import time
import easygui
import csv

if __name__ == '__main__':

    uc = Browser().getBot()
    uc.get("https://www.youtube.com/results?search_query=dog+shorts&sp=EgYIAhABGAE%253D")
    uc.execute_script("window.scrollTo(0, 20000);")
    time.sleep(5)
    uc.execute_script("window.scrollTo(0, 20000);")
    time.sleep(15)
    videoname = (uc.find_elements(By.ID, "video-title")[5]).text
    print(videoname)
    file_input = []
    file_clean = []
    for i in range(1,20):
        file_input.append(uc.find_elements(By.ID, "thumbnail")[i].get_attribute('href'))
    uc.quit()
    for i in range(19):
        if "shorts" in file_input[i]:
            file_clean.append(file_input[i])
    print(len(file_clean))
    print(file_clean)

    file = open(r'C:\Users\Death\Desktop\Main Uploader\DogChannel\links_file.csv', 'w+', newline='', encoding="utf-8")
    write = csv.writer(file)
    for i in range(len(file_clean)):
        x = []
        x.append(file_clean[i])
        write.writerows([x])
    file.close()
    print(len(videoname))
    fuckyoutube = []
    print(len(videoname))
    if len(videoname) > 87:
        videoname = videoname[0:87]
        print(videoname)
    fuckyoutube.append(videoname+" @purrfectdog")
    title_data = []
    title_data.append('title')
    popname = []
    popname.append("More clips on https://www.tiktok.com/@purrfectdog                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            "
                   "   #dog #cute #dogsoftiktok #funny #fyp")
    name_data = []
    name_data.append('description')
    import json

    with open(r'C:\Users\Death\Desktop\Main Uploader\DogChannel\rockets_metadata0.json', 'w+', newline='',encoding="utf-8") as fp:
        res = {title_data[0]: fuckyoutube[0],name_data[0]: popname[0]}
        json.dump(res, fp)

