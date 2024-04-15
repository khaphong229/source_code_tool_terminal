import os

try:
  import requests, pystyle, schedule
except:
  os.system('pip install requests && pip install bs4 && pip install pystyle && pip install schedule')

import sys,re,json,random,datetime, requests
from time import sleep
import threading
from os import path


dt=datetime.datetime.now()
def dk():
   a= "\033[1;32m=\033[1;97m="*30
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.001)
   print()
def delay(dl):
  try:
    for i in range(dl, -1, -1):
       print(s+'\033[1;95mĐang Load Tool Chờ '+str(i)+' Giây [-]          ',end='\r')
       sleep(0.2)
       print(s+'\033[1;94mĐang Load Tool Chờ '+str(i)+' Giây [\]          ',end='\r')
       sleep(0.2)
       print(s+'\033[0;33mĐang Load Tool Chờ '+str(i)+' Giây [|]          ',end='\r')
       sleep(0.2)
       print(s+'\033[1;92mĐang Load Tool Chờ '+str(i)+' Giây [/]          ',end='\r')
       sleep(0.2)
       print(s+'\033[1;97mĐang Load Tool Chờ '+str(i)+' Giây [-]          ',end='\r')
       sleep(0.2)
  except:
     sleep(dl)
     print(dl,end='\r')
s = "\033[1;97m『』"

from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
def ra(a):
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.001)
   print()
os.system('clear')                          
def logo():
    logo = """\033[1;32m
		 /$$   /$$ /$$$$$$$  /$$   /$$
		| $$  /$$/| $$__  $$| $$$ | $$
		| $$ /$$/ | $$  \ $$| $$$$| $$
		| $$$$$/  | $$$$$$$/| $$ $$ $$
		| $$  $$  | $$____/ | $$  $$$$
		| $$\  $$ | $$      | $$\  $$$
		| $$ \  $$| $$      | $$ \  $$
		|__/  \__/|__/      |__/  \__/ """
    ra(logo)
#delay(2)
from pystyle import Box
os.system('clear')
def link1s(link_key):
  api_token = 'e2972a7bea846ba97f94d72d2b95426481c5fe2e'
  api_url = f"https://traffic1s.com/api?api={api_token}&url={link_key}"
  result = requests.get(api_url).json()
  if result['status'] == 'error':
    print(result['message'])
  else:
    print(f"Link lấy key => {result['shortenedUrl']} ")


key_chuan = f"KPN-KEY{int(dt.day)*999*888*16}"

link_key=f"https://kpn-tool.tk/keyfree.php?key={key_chuan}"

ds_key=[]

while True: 
    ktra=path.exists("key_kpn.txt")
    if ktra==True:
        with open("key_kpn.txt") as a:
	        key=a.read()
	        if key==key_chuan or key in ds_key:
	            print("Key đúng")
	            sleep(1)
	            break
	        else:
	            print("Key sai")
	            os.remove("key_kpn.txt")
    else:
        with open("key_kpn.txt",'w') as f:
	        link1s(link_key)
	        key=input("\033[37;1mNhập key: \033[32;1m")
	        f.write(key)
	        if key==key_chuan or key in ds_key:
	            print("Key đúng")
	            sleep(1)
	            break
	        else:
	            print("Key sai")
	            os.remove("key_kpn.txt")
os.system('clear')
dk()
logo()
print()
dk()
print()
print("- - - - - - - - - - - - - TDS - - - - - - - - - - - - - - -")
print()
print(s+"\033[1;92mNhập \033[1;94m[0] \033[1;92mTDS YOUTUBE SUBSCRIBE")
print(s+"\033[1;92mNhập \033[1;94m[1] \033[1;92mTDS INSTAGRAM ĐA LUỒNG")
print(s+"\033[1;92mNhập \033[1;94m[2] \033[1;92mTDS INSTAGRAM ĐA LUỒNG PROXY")
print(s+"\033[1;92mNhập \033[1;94m[3] \033[1;92mTDS AUTO CLICK TIKTOK + TIKTOK NOW")
print(s+"\033[1;92mNhập \033[1;94m[4] \033[1;92mTDS AUTO CLICK TRÊN PC")
print()
print("\033[1;97m- - - - - - - - - - - - - TTC - - - - - - - - - - - - - - - - ")
print()
print(s+"\033[1;92mNhập \033[1;94m[5] \033[1;92mTTC CLICK TYM & FOLLOW TIKTOK")
print(s+"\033[1;92mNhập \033[1;94m[6] \033[1;92mTTC CLICK FOLLOW TIKTOK NOW")
print()
print("\033[1;97m- - - - - - - - - - - - - KHÁC - - - - - - - - - - - - - - -")
print()
print(s+"\033[1;92mNhập \033[1;94m[7] \033[1;92mTOOL AUTO PLAY AND WIN - KIẾM PAYPAL")
print(s+"\033[1;92mNhập \033[1;94m[8] \033[1;92mTOOL HUST MEDIA")
print(s+"\033[1;92mNhập \033[1;94m[9] \033[1;92mTOOL TĂNG SUB MIỄN PHÍ")
print(s+"\033[1;92mNhập \033[1;94m[10] \033[1;92mTOOL LIKE4LIKE")
print()
print("\033[1;97m- - - - - - - - - - - - - ME - - - - - - - - - - - - - - - - -")
print()
print(s+"\033[1;92mFacebook: Khả Phong Nguyễn")
print()
dk()
print()
abc = input(s+"\033[1;92mNhập Số : ")
print()
dk()                                                              
try:
  if abc == "0":
    exec(requests.get("http://kpn-tool.tk/tds/ytb").text)
  if abc == "1":
    exec(requests.get("http://kpn-tool.tk/tds/tdsin").text)
  if abc == "2":
    exec(requests.get("http://kpn-tool.tk/tds/tdsinsprx").text)
  if abc == "3":
    exec(requests.get("http://kpn-tool.tk/tds/tds_click").text)
  if abc == "4":
    exec(requests.get("http://kpn-tool.tk/tds/tdsclickpc").text)


  if abc == "5":
    exec(requests.get("http://kpn-tool.tk/ttc/ttcclick").text)
  if abc == "6":
    exec(requests.get("http://kpn-tool.tk/ttc/ttcnow").text)


  if abc == "7":
    exec(requests.get("http://kpn-tool.tk/play").text)
  if abc == "8":
    exec(requests.get("http://kpn-tool.tk/hust_link").text)
  if abc == "9":
    exec(requests.get("http://kpn-tool.tk/tangsub").text)
  if abc == "10":
    exec(requests.get("http://kpn-tool.tk/l4l").text)
except:
   pass


