import requests
from random import randint
import re
import random

b=open('link_video.txt','r')
list = b.read().splitlines()

h=0

for link_vid in list:
	try:
		#link_vid=input("Nhập link video: ")

		h+=1

		ten=link_vid.split("video/")[1].split("?is_copy_url=1&is_from_webapp=v1")[0]
		

		url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

		querystring = {"url":link_vid}

		headers = {
			"X-RapidAPI-Key": "xxxxxxxxxxxxxxx",
			"X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
		}

		response = requests.request("GET", url, headers=headers, params=querystring)

		#print(response.text)
		videos=response.text
		video=videos.replace('[','')
		link=re.findall(r'{"video":"([^"]+)"',video)
		url_video=''.join(link)
		#print(url_video)
		names=random.randrange(1,10000)
		name='xxxxxxxxxxxxxxx'+str(ten)+'.mp4'
		print(f"{h} <> {name}")
		r=requests.get(url_video)
		with open (name,'wb') as f:
			f.write(r.content)
	except:
		print("Lỗi")
		pass

