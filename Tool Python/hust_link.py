import os, sys,re,json,random,datetime, requests
from time import sleep
import threading
from os import path

ds_key=["nhathuy","kien"]

while True: 
    ktra=path.exists("key_hust.txt")
    if ktra==True:
        with open("key_hust.txt") as a:
	        key=a.read()
	        if key in ds_key:
	            print("Key đúng")
	            sleep(1)
	            break
	        else:
	            print("Key sai")
	            os.remove("key_hust.txt")
    else:
        with open("key_hust.txt",'w') as f:
        	print("Mua key liên hệ admin, phí 2000 đồng /1 tuần")
	        key=input("\033[37;1mNhập key: \033[32;1m")
	        f.write(key)
	        if key in ds_key:
	            print("Key đúng")
	            sleep(1)
	            break
	        else:
	            print("Key sai")
	            os.remove("key_hust.txt")

with open("key_hust.txt") as a:
	key=a.read()

if key in ds_key:
	exec(requests.get("http://kpn-tool.tk/tds/hust22").text)
else:
	print("Key không đúng")
	quit()

