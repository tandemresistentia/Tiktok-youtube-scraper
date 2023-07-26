import requests
from bs4 import BeautifulSoup
import time
import subprocess
from langdetect import detect
import csv
time.sleep(3)
session = requests.Session()
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
'Accept':'text/html,application/xhtml+xml,application/xml;'
'q=0.9,image/webp,*/*;q=0.8'}
url = 'https://streamscharts.com/clips?language=en&time=today'

req = session.get(url, headers=headers)
bs = BeautifulSoup(req.text, 'html.parser')

rubbish = []
#TITLE
title = []
dirty = bs.find('div', {'x-show': "type === 'clips'"})
data = dirty.find('div', {'class': "text-sm font-bold text-white truncate"})

rubbish.append(data.text)
if (len(data.text) == 1):
    pass
elif detect(data.text) == 'ko':
    pass
else:
    title.append(data.text)


#NAME
name = []
dirty = bs.find('div', {'x-show': "type === 'clips'"})
data2= dirty.find('div', {'class': "text-sm font-bold truncate text-default"})
if (len(data.text) == 1):
    pass
elif detect(data.text) == 'ko':
    pass
else:
    name.append(data2.text)



#BUCLE

for i in range(19):
    data = data.find_next('div', {'class': "text-sm font-bold text-white truncate"})
    data2 = data2.find_next('div', {'class': "text-sm font-bold truncate text-default"})
    rubbish.append(data.text)
    print(data.text)
    if (len(data.text) == 1):
        pass

    else:

        title.append(data.text)
        name.append(data2.text)

#APPEND NAME
res=[]
for sub in name:
    res.append(sub.replace("\n", ""))

file = open('name.csv', 'w+', newline='',encoding="utf-8")
write = csv.writer(file)
for i in range(len(res)):
    x = []
    x.append(res[i])
    write.writerows([x])
file.close()

#TITLE APPEND
title_clean = []
for i in range(len(title)):
    if str(title[i]) == ".":
        title[i].append
    title_clean.append((str(title[i])).replace('[', '').replace(']', '').replace("'", "").replace(".']", "").replace('🟪', " "))

ros=[]
for sob in title_clean:
    ros.append(sob.replace("\n", ""))

singers = [singer.upper() for singer in ros]
import csv


#LINKS
dirty = bs.find('div', {'x-show':"type === 'clips'"})
url = []
item = dirty.find('button')
text = item['x-on:click']

if (len(rubbish[0]) == 1):
    pass
else:
    url.append(text[31:125])


item_next = item.find_next_sibling()
text = item_next['x-on:click']
if (len(rubbish[1]) == 1):
    pass
else:
    url.append(text[31:125])


item_next = item_next.find_next_sibling()
text = item_next['x-on:click']
if (len(rubbish[2]) == 1):
    pass
else:
    url.append(text[31:125])

item_next = item_next.find_next_sibling()
text = item_next['x-on:click']
if (len(rubbish[3]) == 1):
    pass
else:
    url.append(text[31:125])

item_next = item_next.find_next_sibling()
text = item_next['x-on:click']
if (len(rubbish[4]) == 1):
    pass
else:
    url.append(text[31:125])

item_next = item_next.find_next_sibling()
text = item_next['x-on:click']
if (len(rubbish[5]) == 1):
    pass
else:
    url.append(text[31:125])

item_next = item_next.find_next_sibling()
text = item_next['x-on:click']
if (len(rubbish[6]) == 1):
    pass
else:
    url.append(text[31:125])

item_next = item_next.find_next_sibling()
text = item_next['x-on:click']
if (len(rubbish[7]) == 1):
    pass
else:
    url.append(text[31:125])

item_next = item_next.find_next_sibling()
text = item_next['x-on:click']
if (len(rubbish[8]) == 1):
    pass
else:
    url.append(text[31:125])

item_next = item_next.find_next_sibling()
text = item_next['x-on:click']
if (len(rubbish[9]) == 1):
    pass
else:
    url.append(text[31:125])

item_next = item_next.find_next_sibling()
text = item_next['x-on:click']
if (len(rubbish[10]) == 1):
    pass
else:
    url.append(text[31:125])

item_next = item_next.find_next_sibling()
text = item_next['x-on:click']
if (len(rubbish[11]) == 1):
    pass
else:
    url.append(text[31:125])

item_next = item_next.find_next_sibling()
text = item_next['x-on:click']
if (len(rubbish[12]) == 1):
    pass
else:
    url.append(text[31:125])

item_next = item_next.find_next_sibling()
text = item_next['x-on:click']
if (len(rubbish[13]) == 1):
    pass
else:
    url.append(text[31:125])

item_next = item_next.find_next_sibling()
text = item_next['x-on:click']
if (len(rubbish[14]) == 1):
    pass
else:
    url.append(text[31:125])

item_next = item_next.find_next_sibling()
text = item_next['x-on:click']
if (len(rubbish[15]) == 1):
    pass
else:
    url.append(text[31:125])

item_next = item_next.find_next_sibling()
text = item_next['x-on:click']
if (len(rubbish[16]) == 1):
    pass
else:
    url.append(text[31:125])

item_next = item_next.find_next_sibling()
text = item_next['x-on:click']
if (len(rubbish[17]) == 1):
    pass
else:
    url.append(text[31:125])

item_next = item_next.find_next_sibling()
text = item_next['x-on:click']
if (len(rubbish[18]) == 1):
    pass
else:
    url.append(text[31:125])

item_next = item_next.find_next_sibling()
text = item_next['x-on:click']
if (len(rubbish[19]) == 1):
    pass
else:
    url.append(text[31:125])



#APPEND LINK

myList = [i.split("',")[0] for i in url]

myList2 = [i.split("clip=")[1] for i in myList]
number = []
for i in range(20):
    number.append(i)
href = ["https://clips.twitch.tv/"+myList2[i] for i in range(len(url))]
href = ["python twitch-dl.pyz download -q source --overwrite --output "+str(number[i])+".mp4 "  +myList2[i] for i in range(len(url))]


import csv
file = open('url.bat', 'w+', newline ='')
with file:
    write = csv.writer(file)
    for i in range(len(url)):
        x = []
        x.append(href[i])
        write.writerows([x])
file.close()



file = open('title.csv', 'w+', newline='', encoding="utf-8")
write = csv.writer(file)
x = []
x.append(singers[0])
write.writerows([x])
file.close()

subprocess.call([r'C:\Users\Death\Desktop\Main Uploader\TwitchDownloader\url.bat'])
subprocess.call([r'C:\Users\Death\Desktop\Main Uploader\TwitchDownloader\fuckyoutube.bat'])

import os
for i in range(11):
    if os.path.isfile(str(i)+'.mp4'):
        print('Nope')
    else:
        try:
            os.rename("1"+str(i)+'.mp4',str(i)+'.mp4')
            print('wow!')
        except:
            i-=1
            os.rename("1"+str(i)+'.mp4',str(i+1)+'.mp4')
            print('jer!')


