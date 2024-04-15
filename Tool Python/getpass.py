import os, re, urllib.parse, sys,requests
from requests import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from time import *
from random import *
from string import *
from datetime import datetime
ss = session()
os.system("clear")
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
def run(link):
	while True:
		try:
			w = ss.get(link,headers={"user-agent":"Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36"},verify=False).text
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
		except:
			input("Reset ip")
while True:
	print ("-"*40)
	s = input("Paste Link: ")
	try:
		link = s.split("u=")[1].replace("cutt.ly","getpass.top")+".html"
	except:
		link = get(s,headers={"user-agent":"Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36"},allow_redirects=False).headers["Location"]
	#print(link)
	r = run(link)
	v = r[0]
	id = r[1]
	code = r[2]
	for z in range(120,-1,-1):
		print("chờ",z,"giây",end=" \r")
		sleep(1)
	if code=="":
		while True:
			r = run(link)
			v = r[0]
			id = r[1]
			code = r[2]
			data = {"get_phone":code,"id":id,"get_check_phone_id":v}
			c = ss.post("https://getpass.top/ajax/ajax_check_phone",data=data,headers={"user-agent":"Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36","referer":link,"X-Requested-With":"XMLHttpRequest"},verify=False).json()["rs_phone"].split(">")[1].split("<")[0]
			if "Bạn đã nhập sai!!!" not in c:
				print(c.replace("\n","").strip())
				text = c.split(': ')[1].split('\n')[0]
				break
	else:
		data = {"get_phone":code,"id":id,"get_check_phone_id":v}
		c = ss.post("https://getpass.top/ajax/ajax_check_phone",data=data,headers={"user-agent":"Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36","referer":link,"X-Requested-With":"XMLHttpRequest"},verify=False).json()["rs_phone"].split(">")[1].split("<")[0]
		if "Bạn đã nhập sai!!!" in c:
			while True:
				r = run(link)
				v = r[0]
				id = r[1]
				code = r[2]
				data = {"get_phone":code,"id":id,"get_check_phone_id":v}
				c = ss.post("https://getpass.top/ajax/ajax_check_phone",data=data,headers={"user-agent":"Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36","referer":link,"X-Requested-With":"XMLHttpRequest"},verify=False).json()["rs_phone"].split(">")[1].split("<")[0]
				if "Bạn đã nhập sai!!!" not in c:
					print(c.replace("\n","").strip())
					text = c.split(': ')[1].split('\n')[0]
					break
		else:
			print(c.replace("\n","").strip())
			text = c.split(': ')[1].split('\n')[0]
	print ("-"*40)
	
1