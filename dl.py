import requests

with open('fansdata1.txt', 'r', encoding='utf-8') as uu: name = uu.readlines()
with open('onlyarr1.txt', 'r', encoding='utf-8') as bname: arr = bname.readlines()
for i in range(0, 75):
    pic_url = arr[i].replace("\n","")
    pic = requests.get(pic_url, timeout=10)
    path=r"F:\face\\" + name[i].replace("\n","")
    with open(path, 'wb') as f0:
        f0.write(pic.content)