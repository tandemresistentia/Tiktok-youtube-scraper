file = open('name.csv', 'w+', newline='',encoding="utf-8")
write = csv.writer(file)
for i in range(len(res)):
    x = []
    x.append(res[i])
    write.writerows([x])
file.close()