import os, re, urllib.parse, sys,requests, schedule,json
from urllib.parse import *
from requests import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from time import *
from random import *
from string import *
from datetime import datetime
red = "\033[31;1m"
green = "\033[32;1m"
yellow = "\033[33;1m"
blue = "\033[36;1m"
pink = "\033[95m"
reset = "\033[0;1m"
ss = session()
os.system("clear")
a = """
  ██████╗  ██████╗   ███╗   ███╗███╗   ███╗ ██████╗ 
██╔════╝ ██╔════╝    ████╗ ████║████╗ ████║██╔═══██╗
██║  ███╗██║         ██╔████╔██║██╔████╔██║██║   ██║
██║   ██║██║         ██║╚██╔╝██║██║╚██╔╝██║██║   ██║
╚██████╔╝╚██████╗    ██║ ╚═╝ ██║██║ ╚═╝ ██║╚██████╔╝
 ╚═════╝  ╚═════╝    ╚═╝     ╚═╝╚═╝     ╚═╝ ╚═════╝ 
                                                    
                                                          """
print(a)                                                          
cookiettc = input("Nhập Cookie TTC:")
authorization = input("Nhập authorization:")
cookieytb = input("Nhập Cookie YTB:")
os.system("clear")
head = {
"cookie":cookiettc,
"referer":"https://tuongtaccheo.com/youtube/kiemtien/subcheo/",
"x-requested-with":"XMLHttpRequest",
"user-agent":"Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Mobile Safari/537.36",
}
a = ss.get("https://tuongtaccheo.com/home.php",headers=head).text
hi = a.split("<h2 class='text-center'>Chào mừng <i>")[1].split("<")[0]
sodu = a.split('id="soduchinh">')[1].split('<')[0]
print(f"Tên Tài Khoản: {hi} | Số Dư: {sodu} Coin")
print("-"*50)
def subyt(link):
	ss = session()
	head = {
	"cookie":cookieytb,
	"user-agent":"Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Mobile Safari/537.36",
	}
	a = ss.get(link,headers=head).text
	id = a.split('channelId":"')[1].split('"')[0]
	link = "https://m.youtube.com/channel/"+id
	print("Link channel:",link)
	vd = ss.get(link,headers=head).text
	d = vd.split('"INNERTUBE_CONTEXT":')[1].split('}},')[0]
	dt = str(int(datetime.now().timestamp())*1000)
	data = '{"context":'+d+'},"adSignalsInfo":{"params":[{"key":"dt","value":"'+dt+'"},{"key":"flash","value":"0"},{"key":"frm","value":"0"},{"key":"u_tz","value":"420"},{"key":"u_his","value":"5"},{"key":"u_h","value":"640"},{"key":"u_w","value":"360"},{"key":"u_ah","value":"640"},{"key":"u_aw","value":"360"},{"key":"u_cd","value":"24"},{"key":"bc","value":"31"},{"key":"bih","value":"560"},{"key":"biw","value":"360"},{"key":"brdim","value":"0,0,0,0,360,0,360,560,360,560"},{"key":"vis","value":"1"},{"key":"wgl","value":"true"},{"key":"ca_type","value":"image"}]}},"channelIds":["'+id+'"],"params":"EgIIAhgA"}'
	data = json.loads(data)
	head = {
	"authorization":authorization,
	"cookie":cookieytb,
	"referer":link,
	"user-agent":"Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Mobile Safari/537.36",
	"x-origin":"https://m.youtube.com",
	}
	sub = ss.post("https://m.youtube.com/youtubei/v1/subscription/subscribe?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false",json=data,headers=head).text
	if "responseContext" in sub:
		print("Đăng Ký Thành Công")
	else:
		print("Đăng Ký Không Thành Công")
def nt(id):
	data = {"id":id}
	nt = ss.post("https://tuongtaccheo.com/youtube/kiemtien/subcheo/nhantien.php",data=data,headers=head).json()
	print(f"\033[32;1m{nt}\033[0;1m")
while True:
	id = ""
	for _ in range(5):
		print("+-"*25)
		job = ss.get("https://tuongtaccheo.com/youtube/kiemtien/subcheo/getpost.php",headers=head)
		idp = job.json()[0]["idpost"]
		link = job.json()[0]["link"].replace("www","m",1)
		id+=idp+","
		subyt(link)
		sleep(20)
	ss.get("https://tuongtaccheo.com/refresh.php",headers=head)
	nt(id[:-1])
	
	







