import urllib.request as request
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context #選擇不用認證此 SSL 憑證，就可以讓 urllib 正常運作
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response)
alist=data["result"]["results"] #alist是列表
with open("data.csv",mode="w",encoding="utf-8") as file:
        for attr in alist:
            urlList=attr["file"].split("https://") #字串轉列表
            urlFirst="".join(urlList[1:2]) #列表轉字串
            file.write(attr["stitle"]+","+attr["address"][5:8]+","+attr["longitude"]+","+attr["latitude"]+","+"https://"+urlFirst+"\n") #字串