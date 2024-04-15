import os, re, urllib.parse, sys,requests, schedule
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
#ua = input("Nhap user-agent:")
#ck = input("Nhap cookie:")
ua = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36"
ck = 'xxx'
print("""Chọn Page để chạy tool !
[1] Đọc Báo Kiếm Tiền
[2] Việc Làm Thêm Tại Nhà Bằng Điện Thoại
[3] Kiếm Tiền Online Bằng Điện Thoại""")
chon = int(input("Chọn chế độ:"))
print("[1] Chạy dùng proxy\n[2] Chạy không dùng proxy")
mode = int(input("Chọn:"))
os.system("clear")
if chon==1:
	id_page = "104671401944796"
if chon==2:
	id_page = "110694223935440"
if chon==3:
	id_page = "112632580605980"
idfb = ck.split("c_user=")[1].split(";")[0]
head = {
"cookie":ck,
}
def get_proxy():
	p = post("https://tmproxy.com/api/proxy/get-new-proxy",json={"api_key":"3b5d6d3553448b64b4098dbbaea603bc","id_location":1}).json()
	p = p['data']['socks5']
	proxy = {
	'http':f'socks5://{p}',
	'https':f'socks5://{p}',
	}
	return proxy
def send(text):
	mes = get(f"https://mbasic.facebook.com/messages/read/?tid=cid.c.{idfb}%3A{id_page}",headers=head).text
	fb_dtsg = mes.split('name="fb_dtsg" value="')[1].split('"')[0]
	jazoest = mes.split('name="jazoest" value="')[1].split('"')[0]
	csid = mes.split('name="csid" value="')[1].split('"')[0]
	data = {
	"fb_dtsg":fb_dtsg,
	"jazoest":jazoest,
	"body":text,
	"send":"Gửi",
	"tids":f"cid.c.{idfb}:{id_page}",
	"wwwupp":"C3",
	f"ids[{id_page}]":f"{id_page}",
	"referrer":"",
	"ctype":"",
	"cver":"legacy",
	"csid":csid,
	}
	send = post("https://mbasic.facebook.com/messages/send/",data=data,headers=head,allow_redirects=False)
	print("Send Code Success!")
def mess():
	x = 0
	while True:
		try:
			x+=1
			if x==5:
				x=0
				input("Click tim nv")
			sleep(5)
			mes = get(f"https://mbasic.facebook.com/messages/read/?tid=cid.c.{idfb}%3A{id_page}",headers=head).text
			link = mes.split('target="_blank">')[1].split('<')[0]
			link = unquote(link).replace("&shy;","")
			if link=="hãy cho chúng tôi biết":
				exit("Acc fb đã bị chặn mess! https://mbasic.facebook.com/messages/")
			return unquote(link)
			break
		except:
			pass
def gc(tt,sor,code):
	dt = datetime.now()
	d=int(dt.strftime("%d"))
	h=int(dt.strftime("%H"))
	m=int(dt.strftime("%M"))
	t=sor*(round((m+7)/tt)+d*h)
	ma=code+str(t)
	return ma
def gc1(tt,sor,code):
	dt = datetime.now()
	d=int(dt.strftime("%d"))
	h=int(dt.strftime("%H"))
	m=int(dt.strftime("%M"))
	t=sor*(round(m/tt)+d*h)
	ma=code+str(t)
	return ma
def run(link,proxy,mode):
	while True:
		try:
			if mode==1:
				w = ss.get(link,headers={"user-agent":ua},proxies=proxy,verify=False).text
			else:
				w = ss.get(link,headers={"user-agent":ua},verify=False).text
			s = w.split('</span> thì bấm vào đó</li>')[0].split('>')[-1].split(".")[0]
			v = w.split('<input type="hidden" value="')[1].split('"')[0]
			id = w.split('<input type="hidden" value="')[2].split('"')[0]
			print(s,v,id)
			if "Vinhomeoceanpark" == s:
				code = gc(15,86,"V")
			elif "Kingcamera" == s:
				code = gc1(16,99,"K")
			elif "oceanparkvinhomes" == s:
				code = gc1(15,89,"P")
			elif "Casauhoaca" == s:
				code = gc(30,83,"H")
			elif "Antinphat" == s:
				code = gc1(17,84,"ATP")
			elif "Noithatahome" == s:
				code = gc(15,89,"G")
			elif "Chiase1" == s:
				code = gc1(18,68,"C")
			elif "Casaukieuhung" == s:
				code = gc(15,84,"K")
			elif "Buffseo" == s:
				code = gc(10,82,"BUF")
			elif "Skillking" == s:
				code = gc(30,89,"F")
			elif "Top10phanmem" == s:
				code = gc(16,10,"T")
			elif "Vinhomesdreamcityhungyen" == s:
				code = gc(15,87,"Q")
			elif "Vincomquangtri" == s:
				code = gc(15,87,"Q")
			elif "Hungluxury" == s:
				code = gc(11,83,"GLU")
			elif "Simcuatui" == s:
				code = gc(10,94,"M")
			elif "Tongdaiviettel" == s:
				code = gc(12,94,"V")
			elif "Mayphunsonwagner":
				code = gc(12,99,"W")
			elif "Thuexedulich6789":
				code = gc(10,89,"C")
			elif "Fpttelecom":
				code = gc(12,92,"D")
			elif "Giaydankinhnnd":
				code = gc(11,87,"G")
			elif "Caosangauto":
				code = gc(11,91,"C")
			elif "Suckhoe123":
				code = gc(12,99,"W")
			elif "Atoztravel" == s:
				code = gc(10,85,"ATO")
			elif "Thuexedulich6789" == s:
				code = gc(10,89,"EDU")
			elif "Luatgiakhang" == s:
				code = gc(10,85,"AKH")
			elif "Sanbaokim" == s:
				code = gc(10,7,"K")
			elif "Danhantaodupont" == s:
				code = gc(10,85,"DUP")
			elif "xxxx":
				code = gc(12,99,"W")
			elif "xxxx":
				code = gc(12,99,"W")
			else:
				code = ""
			return [v,id,code]
			break
		except:
			if mode==1:
				pass
			else:
				input("Reset ip")
if mode==1:
	proxy = get_proxy()
	x = 0
while True:
	try:
		s = mess()
		s = input("Nhập link: ")
		if mode==1:
			if x==5:
				x = 0
				proxy = get_proxy()
			link = get(s,headers={"user-agent":ua},proxies=proxy,allow_redirects=False).headers["Location"]
		else:
			link = get(s,headers={"user-agent":ua},allow_redirects=False).headers["Location"]
		print ("-"*40)
		print(link)
		for _ in range(120,-1,-1):
			print("Wait",_,end=" \r")
			sleep (1)
		if mode==1:
			r = run(link,proxy,1)
		else:
			r = run(link,"",2)
		v = r[0]
		id = r[1]
		code = r[2]
		if code=="":
			while True:
				try:
					if mode==1:
						r = run(link,proxy,1)
					else:
						r = run(link,"",2)
					v = r[0]
					id = r[1]
					code = r[2]
					data = {"get_phone":code,"id":id,"get_check_phone_id":v}
					if mode==1:
						c = ss.post("https://getpass.top/ajax/ajax_check_phone",data=data,proxies=proxy,headers={"user-agent":ua,"referer":link,"X-Requested-With":"XMLHttpRequest"},verify=False).json()["rs_phone"].split(">")[1].split("<")[0]
					else:
						c = ss.post("https://getpass.top/ajax/ajax_check_phone",data=data,headers={"user-agent":ua,"referer":link,"X-Requested-With":"XMLHttpRequest"},verify=False).json()["rs_phone"].split(">")[1].split("<")[0]
					if "Bạn đã nhập sai!!!" not in c:
						print(c.replace("\n","").strip())
						text = c.split(': ')[1].split('\n')[0]
						send(text)
						break
				except:
					pass
		else:
			data = {"get_phone":code,"id":id,"get_check_phone_id":v}
			if mode==1:
				c = ss.post("https://getpass.top/ajax/ajax_check_phone",data=data,proxies=proxy,headers={"user-agent":ua,"referer":link,"X-Requested-With":"XMLHttpRequest"},verify=False).json()["rs_phone"].split(">")[1].split("<")[0]
			else:
				c = ss.post("https://getpass.top/ajax/ajax_check_phone",data=data,headers={"user-agent":ua,"referer":link,"X-Requested-With":"XMLHttpRequest"},verify=False).json()["rs_phone"].split(">")[1].split("<")[0]
			if "Bạn đã nhập sai!!!" in c:
				while True:
					try:
						if mode==1:
							r = run(link,proxy,1)
						else:
							r = run(link,"",2)
						v = r[0]
						id = r[1]
						code = r[2]
						data = {"get_phone":code,"id":id,"get_check_phone_id":v}
						if mode==1:
							c = ss.post("https://getpass.top/ajax/ajax_check_phone",data=data,proxies=proxy,headers={"user-agent":ua},verify=False).json()["rs_phone"].split(">")[1].split("<")[0]
						else:
							c = ss.post("https://getpass.top/ajax/ajax_check_phone",data=data,headers={"user-agent":ua},verify=False).json()["rs_phone"].split(">")[1].split("<")[0]
						if "Bạn đã nhập sai!!!" not in c:
							print(c.replace("\n","").strip())
							text = c.split(': ')[1].split('\n')[0]
							send(text)
							break
					except:
						pass
			else:
				print(c.replace("\n","").strip())
				text = c.split(': ')[1].split('\n')[0]
				send(text)
		if mode==1:
			x+=1
		print ("-"*40)

	except:
		pass




