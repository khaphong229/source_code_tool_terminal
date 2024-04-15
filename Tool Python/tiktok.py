import requests
from random import randint
import re
import random

b=open('linh.txt','r')
list = b.read().splitlines()

h=0

for link_vid in list:
	try:
		#link_vid=input("Nhập link video: ")

		h+=1

		ten=link_vid.split("video/")[1]
		

		url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

		querystring = {"url":link_vid}

		headers = {
			"X-RapidAPI-Key": "7d2fe61d12msha2ef10485a516a3p1f5bf4jsn2cb9e4e81c12",
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
		name='linh/'+str(ten)+'.mp4'
		print(f"{h} <> {name}")
		r=requests.get(url_video)
		with open (name,'wb') as f:
			f.write(r.content)
	except:
		print("Lỗi")
		pass

