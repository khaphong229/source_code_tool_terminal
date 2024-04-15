import os, re, urllib.parse, sys
from requests import *
from time import *
import requests
from random import *
from string import *
from datetime import datetime
def  cls():
	os.system('cls' if os.name == 'nt' else 'clear')
def delay(dl):
	for _ in range(randint(dl,dl+15),-1,-1):
		print(f"{reset}                        ",end=" \r")
		sleep(0.25)
		print(f"{yellow}Chờ",end=" \r")
		sleep(0.25)
		print(f"{blue}Chờ",_,end=" \r")
		sleep(0.25)
		print(f"{green}Chờ",_,"giây",end=" \r")
		sleep(0.25)
def getck(name):
	ck = []
	for x in name:
		ck.append(x.name+"="+x.value+";")
	ck=''.join(ck)
	return ck
cls()
red = "\033[31;1m"
green = "\033[32;1m"
yellow = "\033[33;1m"
blue = "\033[36;1m"
pink = "\033[95m"
reset = "\033[0;1m"
try:
	f=open("ckig.txt")
	soacc = len(f.readlines())
	f.close()
except:
	soacc = 0
if soacc==0:
	#if not os.path.exists("proxy.txt"):
	fp = open("proxy.txt","w")
	f=open("ckig.txt","w")
	soacc = int(input("Nhập số acc muốn chạy: "))
	cls()
	for a in range(soacc):
		print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
		f.write(input(f"\033[33;1mNhap cookie cho acc {a+1}:")+"\n")
		fp.write(input(f"\033[32;1mNhap proxy cho acc {a+1}:")+"\n")
		print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
	f.close()
	fp.close()
	cls()
try:
	f = open("token.txt")
	token = f.read()
	f.close()
except:
	token = input("Nhap Token Tds:")
	f = open("token.txt","w")
	f.write(token)
	f.close()
max_job = int(input("Bao nhiêu job thì đổi acc:"))
dl = int(input("Nhập delay:"))
cls()
def ig(id,link,job,ck,proxy):
	#try:
	p = proxy.split(':user')
	proxy = {"http": f"http://user{p[1]}@{p[0]}","https":f"http://user{p[1]}@{p[0]}"}
	csrftoken = ck.split('csrftoken=')[1].split(';')[0]
	if job==1:
		url = f"https://www.instagram.com/web/friendships/{id}/follow/"
	else:
		url = f'https://www.instagram.com/web/likes/{id}/like/'
	head = {
	"Host":"www.instagram.com",
	"content-type":"application/x-www-form-urlencoded",
	"content-length":"0",
	"x-instagram-ajax":"1006033878",
	"x-asbd-id":"198387",
	"x-ig-app-id":"1217981644879628",
	"x-requested-with":"XMLHttpRequest",
	"user-agent":"Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Mobile Safari/537.36",
	"x-csrftoken":csrftoken,
	"cookie":ck,
	}
	r = post(url,data="",proxies=proxy,headers=head)
	#'Content-Length'#'Content-Type'
	try:
		if r.json()["status"]=="ok":
			mess = f"{green}SUCCESS ~ {blue}LIKE ~ {yellow}{id} ~ {pink}{link}" if job!=1 else f"{green}SUCCESS ~ {blue}FOLLOW ~ {yellow}{id} ~ {pink}{link}"
		else:
			mess = f"{red}ERROR ~ {blue}LIKE ~ {yellow}{id} ~ {pink}{link}" if job!=1 else f"{red}ERROR ~ {blue}FOLLOW ~ {yellow}{id} ~ {pink}{link}"
	except:
		mess = f"{red}ERROR ~ {blue}LIKE ~ {yellow}{id} ~ {pink}{link}" if job!=1 else f"{red}ERROR ~ {blue}FOLLOW ~ {yellow}{id} ~ {pink}{link}"
	return mess
	#except:
		#pass
def tongxu():
	return get(f"https://traodoisub.com/api/?fields=profile&access_token={token}").json()["data"]["xu"]
while True:
	for i in range(soacc):
		file_prx = open("proxy.txt")
		file_ck=open("ckig.txt")
		ckig = file_ck.readlines()[i].strip()
		idig = ckig.split("ds_user_id=")[1].split(";")[0]
		proxy = file_prx.readlines()[i].strip()
		file_prx.close()
		file_ck.close()
		headig = {
		"Host":"www.instagram.com",
		"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"accept-language":"vi-VN,en-US;q=0.8",
		"user-agent":"Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Mobile Safari/537.36",
		"cookie":ckig,
		}
		if ckig=="":
			continue
		check = get("https://www.instagram.com/",headers=headig)
		if "Tạo một tài khoản hoặc đăng nhập Instagram" in check.text:
			continue
		elif "checkpoint_url" in check.url:
			continue

		lay=requests.get("https://www.instagram.com/",headers=headig).text
		idacc=lay.split('username')[1].split('badge_count')[0].split('\"')[2].split('\\')[0]

		datnick = get(f"https://traodoisub.com/api/?fields=instagram_run&id={idig}&access_token={token}").json()
		if 'error' not in datnick:
			print(f"{reset}Đặt cấu hình thành công id {idig} ! <> {idacc}")
		else:
			print(f"{datnick['error']} <> {idacc}")
			continue
		def like():
			try:
				nv_like = get(f"https://traodoisub.com/api/?fields=instagram_like&access_token={token}").json()
				if nv_like["data"]==[]:
					print(f"{red}Hết job like ...",end=" \r")
					sleep(1)
				else:
					id = nv_like["data"][0]["id"]
					idd = id.split("_")[0]
					link = nv_like["data"][0]["link"]
					tt = ig(idd,link,0,ckig,proxy)
					print("\033[33;1m-\033[32;1m-\033[31;1m-\033[36;1m-"*15)
					print(tt)
					if 'SUCCESS' in tt:
						duyet = get(f"https://traodoisub.com/api/coin/?type=INS_LIKE_CACHE&id={id}&access_token={token}").json()
						if 'success' in duyet:
							print(f'{blue}TDS ~ {green}{duyet["data"]["msg"]} xu ~ {yellow}Chờ duyệt: {duyet["data"]["pending"]} xu ~ {green}Tổng xu: {tongxu()} xu')
						else:
							print(duyet)
					print("\033[33;1m-\033[32;1m-\033[31;1m-\033[36;1m-"*15)
			except:
				pass
		def follow():
			try:
				nv_like = get(f"https://traodoisub.com/api/?fields=instagram_follow&access_token={token}").json()
				if nv_like["data"]==[]:
					print(f"{red}Hết job follow ...",end=" \r")
					sleep(1)
				else:
					id = nv_like["data"][0]["id"]
					idd = id.split("_")[0]
					link = nv_like["data"][0]["link"]
					#print(f"{blue}FOLLOW ~ {yellow}{idd} ~ {pink}{link}")
					tt = ig(idd,link,1,ckig,proxy)
					print("\033[33;1m-\033[32;1m-\033[31;1m-\033[36;1m-"*15)
					print(tt)
					if 'SUCCESS' in tt:
						duyet = get(f"https://traodoisub.com/api/coin/?type=INS_FOLLOW_CACHE&id={id}&access_token={token}").json()
						if 'success' in duyet:
							print(f'{blue}TDS ~ {green}{duyet["data"]["msg"]} xu ~ {yellow}Chờ duyệt: {duyet["data"]["pending"]} xu ~ {green}Tổng xu: {tongxu()} xu')
						else:
							print(duyet)
					print("\033[33;1m-\033[32;1m-\033[31;1m-\033[36;1m-"*15)
			except:
				pass
		j = 0
		while j<max_job:
			j+=2
			like()
			delay(dl)
			follow()
			delay(dl)
			

