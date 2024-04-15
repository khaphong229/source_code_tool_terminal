import os, re, urllib.parse, sys,requests, schedule,json
from urllib.parse import *
from requests import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from time import *
from random import *
from string import *
from datetime import datetime
ss = session()
os.system("clear")

#tk=input("Nhập tk tds: ")
#mk=input("Nhập mk tds: ")
ck_tds=input("Nhập cookie tds: ")
chon=int(input("[1] SUB | [2] CMT || => "))

os.system("clear")

a=input("Nhập id kênh sau / của link kênh: ")
aut=input("Nhập authorization: ")
ck=input("Nhập cookie: ")

os.system("clear")

#tc = ss.get("https://traodoisub.com/",headers={"user-agent":"Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Mobile Safari/537.36"})
#ck_tds= tc.headers['set-cookie'].split(';')[0]
#log = ss.post("https://traodoisub.com/scr/login.php",data={"username":tk,"password":mk},headers={"user-agent":"Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Mobile Safari/537.36","x-requested-with":"XMLHttpRequest","cookie":ck_tds})
#if "success" not in log.text:
	#exit("Sai TK hoặc MK!")

head = {
"cookie":ck_tds,
"user-agent":"Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Mobile Safari/537.36",
}

def subyt(link,aut,ck):
	ss = session()
	head = {
	"cookie":ck,
	"user-agent":"Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Mobile Safari/537.36",
	}
	vd = ss.get(link,headers=head).text
	id = link.split("/channel/")[1]
	d = vd.split('"INNERTUBE_CONTEXT":')[1].split('}},')[0]
	dt = str(int(datetime.now().timestamp())*1000)
	data = '{"context":'+d+'},"adSignalsInfo":{"params":[{"key":"dt","value":"'+dt+'"},{"key":"flash","value":"0"},{"key":"frm","value":"0"},{"key":"u_tz","value":"420"},{"key":"u_his","value":"5"},{"key":"u_h","value":"640"},{"key":"u_w","value":"360"},{"key":"u_ah","value":"640"},{"key":"u_aw","value":"360"},{"key":"u_cd","value":"24"},{"key":"bc","value":"31"},{"key":"bih","value":"560"},{"key":"biw","value":"360"},{"key":"brdim","value":"0,0,0,0,360,0,360,560,360,560"},{"key":"vis","value":"1"},{"key":"wgl","value":"true"},{"key":"ca_type","value":"image"}]}},"channelIds":["'+id+'"],"params":"EgIIAhgA"}'
	data = json.loads(data)
	head = {
	"authorization":aut,
	"cookie":ck,
	"referer":link,
	"user-agent":"Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Mobile Safari/537.36",
	"x-origin":"https://m.youtube.com",
	}
	sub = ss.post("https://m.youtube.com/youtubei/v1/subscription/subscribe?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false",json=data,headers=head).text


if chon==1:

	def datn(a):
		name = ss.get("https://traodoisub.com/view/chyoutube/",headers=head).text.split(a)[2].split("</span></td>")[0].split(">")[-1]
		dat = ss.post("https://traodoisub.com/scr/youtube_datnick.php",data={"iddat":a},headers=head).text
		return name
	def nt():
		print("-"*60)
		data = {"key":"0257272C744254"}
		nt = ss.post("https://traodoisub.com/ex/youtube_follow/nhantien.php",data=data,headers=head).json()
		if nt["code"]!="error":
			msg = nt["msg"]
			xu = nt["xu"]
			print(f'{msg} | {xu} xu'.center(60))
			print("-"*60)

	def sub_yt(link, ck, aut):
		head={
		'Host':'api.kpb-fia.com',
		'User-Agent':'Mozilla/5.0 (Linux; Android 9; RMX1811) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
		'Accept':'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
		}

		data_sub={
		"KPB":"YOUTUBE",
		"TYPE":"SUBSCRIBE",
		"LINK-CHANNEL":link,
		"COOKIE":ck,
		"AUTHORIZATION":aut,
		}
		#print(data_cmt)
		sub=ss.post("https://api.kpb-fia.com/api/kpb-coder.php",data=data_sub,headers=head).json()
		#print(sub)
		if sub['kpb-check']=="1":
			return True
		else:
			return False

	nv = 0
	acc = datn(a)
	while True:
		while True:
				job = ss.get("https://traodoisub.com/ex/youtube_follow/load.php",headers=head)
				if int(job.json()["cache"])>=3:
					nt()
				#print(job.json())
				if "error" in job.json():
					if int(job.json()["cache"])>0:
						nt()
					break
				elif job.json()['data']==[]:
					print("Hết job rồi",end=" \r")
					break
				else:
					print("-"*60)
					print(f"Đang chạy acc <> {acc}")
					nv+=1
					id = job.json()["data"][0]["id"]
					idd = id.split("__")[1]
					link = "https://m.youtube.com/channel/"+idd
					time = datetime.now().strftime("%H:%M")
					print(f'{time} <> Đăng Ký <> {idd}')
					for _ in range(20,-1,-1):
							print("                        ",end=" \r")
							sleep(0.25)
							print("Chờ",end=" \r")
							sleep(0.25)
							print("Chờ",_,end=" \r")
							sleep(0.25)
							print("Chờ",_,"giây",end=" \r")
							sleep(0.25)
					#subyt(link,aut,ck)
					sub_yt(link,ck,aut)
					cache = ss.post("https://traodoisub.com/ex/youtube_follow/cache.php",data={"id":id,"type":"follow"},headers=head).json()["cache"]
					if int(cache)>=3:
						nt()

elif chon==2:
	def comment_yt(url, msg, ck, aut):
		head={
		'Host':'api.kpb-fia.com',
		'User-Agent':'Mozilla/5.0 (Linux; Android 9; RMX1811) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
		'Accept':'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
		}

		data_cmt={
		'TYPE':'COMMENT',
		'LINK-VIDEO': url,
		'MESSAGE':msg,
		'COOKIE':ck,
		'AUTHORIZATION':aut,
		}
		#print(data_cmt)
		cmt=ss.post("https://api.kpb-fia.com/api/Youtubes.php",data=data_cmt,headers=head).text
		#print(cmt)
		if "success" in cmt:
			return True
		else:
			return False

	def datn(a):
		try:
			name = ss.get("https://traodoisub.com/view/chyoutube/",headers=head).text.split(a)[2].split("</span></td>")[0].split(">")[-1]
			dat = ss.post("https://traodoisub.com/scr/youtube_datnick.php",data={"iddat":a},headers=head).text
			return name
		except:
			return False
	def nt(id):
		head = {
		"host":"traodoisub.com",
		"content-length":"49",
		"content-type":"application/x-www-form-urlencoded; charset=UTF-8",
		"cookie":ck_tds,
		"user-agent":"Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Mobile Safari/537.36",
		}
		try: 

			data = f"id={id}&type=comment"
			nt = ss.post("https://traodoisub.com/ex/youtube_comment/nhantien.php",data=data,headers=head).text

			#user=ss.get("https://traodoisub.com/scr/user.php",headers=head).json()
			#print(user)

			if "2" in nt:
				#print(f'\033[32;1mNhận 1000 xu'.center(60))
				#print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
				return True
			if msg=="Nhận thành công 0 xu":
				return False
		except:
			return False


	nv = 0
	acc = datn(a)
	print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
	print(f"\033[33;1m[{acc} <> {a}]".center(60))
	print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
	while True:
		while True:
			try:
				job = ss.get("https://traodoisub.com/ex/youtube_comment/load.php",headers=head)
				#print(job.json())
				if job.json()['data']==[]:
					print("Hết job ...",end=" \r")
					break
				else:
					#print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
					#print(f"\033[33;1m[{acc} <> {i}]".center(60))
					nv+=1
					id = job.json()["data"][0]["id"]
					url=job.json()["data"][0]["link"]
					uu=url.split("https://www.youtube.com/watch?v=")[1]
					msg=job.json()["data"][0]["msg"]
					time = datetime.now().strftime("%H:%M")

					check=comment_yt(url, msg, ck, aut)
					sleep(3)
					nhan=nt(id)

					user=ss.get("https://traodoisub.com/scr/user.php",headers=head).json()
					xu=user['xu']
					if check==True and nhan==True:
						print(f'\033[0;1m[{nv}] <> \033[36;1m[{time}] <> \033[32;1m[{uu}] <> \033[36;1m[SUCCESS] <> \033[31;1m[{xu}]')
					else:
						print(f'\033[0;1m[{nv}] <> \033[36;1m[{time}] <> \033[32;1m[{uu}] <> \033[36;1m[FAIL] <> \033[31;1m[{xu}]')

					for _ in range(20,-1,-1):
							print("                        ",end=" \r")
							sleep(0.25)
							print("Chờ",end=" \r")
							sleep(0.25)
							print("Chờ",_,end=" \r")
							sleep(0.25)
							print("Chờ",_,"giây",end=" \r")
							sleep(0.25)
					
			except:
				break

else:
	print("Nhập sai")
	quit()