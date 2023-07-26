import csv

with open('title.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    title = list(csv_reader)
with open('name.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    name = list(csv_reader)

sep = "!"
title_clean = []
for i in range(len(title)):
    title[i] = str(title[i]).split(sep, 1)[0]
    title_clean.append((str(title[i])).replace('[', '').replace(']', '').replace("'", "").replace("'", "").replace('🟪', " ")
                       .replace('Ÿ', "").replace('ð', "").replace('©', "").replace('â', "").replace('™T', "")
                       .replace('  ', "").replace('Žƒ', "").replace('˜\\xad', " ").replace('‘', "").replace('€', " "))
print(title_clean[0])
name_clean = []
for i in range(len(name)):
    name_clean.append((str(name[i])).replace('[', '').replace(']', '').replace("'", "").replace("'", ""))



fuckyoutube = []

for i in range(len(title)):
    fuckyoutube.append(str(title_clean[i]))

title_data = []
for i in range(len(title)):
    title_data.append('title')

popname = []


popname.append("More clips on https://www.tiktok.com/@vapetwitch                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            "
               "   #Twitch #TwitchClips #Shorts #"+str(name_clean[0])+" #"+str(name_clean[1])+" #"+str(name_clean[2])+" #"
               +str(name_clean[3])+" #"+str(name_clean[4])+" #"+str(name_clean[5])+" #"+str(name_clean[6])+" #"+str(name_clean[7])+" #"
               +str(name_clean[8])+" #"+str(name_clean[9])+" #"+str(name_clean[10])+" #"+str(name_clean[11])+" #"+str(name_clean[12])+" #"
               +str(name_clean[13])+" #"+str(name_clean[14])+" ")

name_data = []
for i in range(len(title)):
    name_data.append('description')

import json

with open('rockets_metadata0.json', 'w+', newline='',encoding="utf-8") as fp:
    res = {title_data[0]: fuckyoutube[0],name_data[0]: popname[0]}
    json.dump(res, fp)





