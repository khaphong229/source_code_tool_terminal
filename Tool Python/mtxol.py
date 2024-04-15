import os, requests, re, urllib.parse, sys
from bs4 import BeautifulSoup as bs
from time import *
from random import *
from datetime import datetime
red = "\033[31;1m"
green = "\033[32;1m"
yellow = "\033[33;1m"
blue = "\033[36;1m"
pink = "\033[95m"
reset = "\033[0;1m"
mdo="\033[31m";

mtrang="\033[37m";
mxanh="\033[92m";
mvang="\033[93m";
mxanhhd="\033[96m";ss = requests.session()
os.system('clear')
ck = input(mvang+"Nhập Cookie:")
# ck="_ga=GA1.2.1163858725.1696553468; _gid=GA1.2.1203110150.1696727600; PHPSESSID=e99c771e5004593c01f17560ddcc8166; _gat_gtag_UA_129751141_1=1; useragent=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNy4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTcuMC4yMDQ1LjQ3; "
sleep(1)
os.system('clear')
head = {
'Host':'mtxgame.online',
'user-agent':'Mozilla/5.0 (Linux; Android 10; RMX2194) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36',
'cookie':ck,
}
h = ss.get("https://mtxgame.online",headers=head).text
link_nv = re.findall('https://mtxgame.online/play/.*?"',h)[0].replace('"','')
x = 0
while True:
	nv = ss.get(link_nv,headers=head).text
	sdc = nv.split('Số điểm hiện tại:')[1].split('-')[0].replace(' ','').split('<td>')[1].replace('\n','')
	sdc = int(sdc)
	tenn=nv.split('Tên:')[1].split('Số điểm')[0].split('<td>')[1].split('</td>')[0].replace('\n','').replace(' ','')
	con=re.findall('bạn còn.*? lượt',nv)[0].replace("'",'').replace("'",'').replace('bạn còn','').replace('lượt','')
	str1=("💰")
	str2=("👹")
	
	hi = """\033[92m╔═════════════════════╗﻿ 
  \033[95mBắt Đầu Làm Việc 👿
\033[92m╚═════════════════════╝"""
	print(hi)
	print(mxanh+f"Tên Mtxgames.Online:",mvang+(tenn))
	print(mxanh+f"Số Điểm:",mvang+str(sdc) + (str1))
	print(mxanh+"Lượt",mvang+str(con) + (str2))
	#try:
	w = str(nv.split('>Copy<')[1].split('<ul')[0].split("<td>")[1].replace(' ','').replace("\n",""))
	k =  nv.split('linkRef">')[1].split('<')[0]
	print(mxanhhd+"Từ Khóa Cần Tìm Là:",k)
	
  
	#except:òn'
		#exit()
	id = re.findall('name="assignment_id" value=".*?"',nv)[0].split('value="')[1].split('"')[0]
	token = re.findall('name="_token" value=".*?"',nv)
	tk_nt = token[0].split('value="')[1].split('"')[0]
	tk_bq = token[1].split('value="')[1].split('"')[0]

    
	k =  nv.split('linkRef">')[1].split('<')[0]
	con=re.findall('bạn còn.*? lượt',nv)[0].replace("'",'').replace("'",'').replace('bạn còn','').replace('lượt','')
	if "Website:MinhĐức" == w:
	   url="wirvddwca1op"
	if "Website:HưngPhát" == w:
	   url="brp05vlbqdns"
	if "Website:TríBảo" == w:
	   url="mpjglqkh21m8"
	if "Website:BảoPhát" == w:
	   url="mi22rp64jo0n"
	if "Website:ĐạiPhát" == w:
	   url="uui74sqrnsgc"
	if "Website:HòaPhát" == w:
	   url="v9i5kj09f32g"
	if "Website:PhátĐạt" == w:
	   url="whbhtyt9rh4y"
	if "Website:CườngPhát" == w:
	   url="xg9jtq5rh446"
	if "Website:ThịnhPhát" == w:
	   url="z84hxssxviu3"
	if "Website:ĐứcBảo" == w:
	   url="dy2jz01a2okp"
	if "Website:Quangphát" == w:
	   url="4e96vjjkw4e4"
	if "Website:TiếnPhát" == w:
	   url="ubozic5r64xk"
	if "Website:ToànPhát" == w:
	   url="lw1k5uxzmqt2"
	if "Website:VĩnhPhát" == w:
	   url="3xbzsgg5y4ft"
	if "Website:ThịnhĐạt" == w:
	   url="oykz4jpgr8ge"
	if "Website:BảoMinh" == w:
	   url="ynv2uno6rkfy"
	if "Website:QuangMinh" == w:
	   url="apb2n8dj9ct8"
	if "Website:ThuậnPhát" == w:
	   url="lic5bbykfh0o"
	if "Website:VạnPhát" == w:
	   url="5e05faiygzdn"
	if "Website:LộcPhát" == w:
	   url="r3mn55ltz4ss"
	if "Website:PhátĐạtChấminfo" == w:
	   url="whbhtyt9rh4y"
	if "Website:TiếnMinh" == w:
	   url="gitvfz5b69hw"
	else:
	   pass
	coo = "https://mtxgame.online/getcode?key="+url
	code = ss.get(coo).json()['code']
	data_nt = {
	"code":code,
	"assignment_id":id,
	"_token":tk_nt,
	}
	data_bq = {
	"assignment_id":id,
	"_token":tk_bq,
	}
	for _ in range(randint(60,70),-1,-1):
		 print("Chờ",_,"giây",end=" \r")
		 sleep(1)
	print(mvang+ "Code tìm được:",mxanh+str(code))
	nt = ss.post("https://mtxgame.online/submit_code",data=data_nt,headers=head).text
	nv = ss.get(link_nv,headers=head).text

	sdm = nv.split('Số điểm hiện tại:')[1].split('-')[0].replace(' ','').split('<td>')[1].replace('\n','')
	sdm = int(sdm)
	strZ=("💰")
	strS=("😭")
	if sdm > sdc:
		x += 1
		now = datetime.now().strftime("%H:%M:%S")
		print(pink+"Job đã trúng:",x,(strZ))
		print(mxanhhd+f"Mã trúng thưởng bạn đang có là:",mvang+str(sdm),(strZ))
	else:
		print(mdo+"Mã  không trúng thưởng",(strS))
	try:
		sys.exit()
	except:
		pass