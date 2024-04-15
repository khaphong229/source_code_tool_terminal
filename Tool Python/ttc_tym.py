import requests as ss
import os
from time import sleep
import os.path
from os import path
import json
from datetime import datetime
import time, uuid, binascii
import subprocess, re
import platform
from urllib.parse import urlencode
os.system("clear")
head_hit= {
"Content-type": "application/x-www-form-urlencoded"
}
dsapi=[]
ktra=path.exists("api_kpn.txt")
if ktra==True:
		#print(user)
	sua=input(f"\033[37;1mBạn có muốn sửa api không (y/n): \033[32;1m") 
	if sua=="y":
		os.remove("api_kpn.txt")
		a=open('api_kpn.txt','w')
		api=input("Nhập api TTC: ")
		a.write(api)
		a.close()
	else:
		a=open('api_kpn.txt','r')
		api=a.readline()
else:
	a=open('api_kpn.txt','w')
	api=input("Nhập api TTC: ")
	a.write(api)
	a.close()
os.system("clear")

ck_ttc=ss.post("https://tuongtaccheo.com/logintoken.php",data={"access_token":api}).headers['set-cookie'].split(';')[0]
head = {
"cookie":ck_ttc,
"Host":"tuongtaccheo.com",
"x-requested-with":"XMLHttpRequest",
"user-agent":"Mozilla/5.0 (Linux; Android 10; Active 3 Build/QP1A.190711.020;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36",
}
#lấy thông tin
print("\033[32;1mTOOL TTC TIKTOK BY KPN".center(60))
print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
tkk=ss.post(f"https://tuongtaccheo.com/logintoken.php",headers=head,data={"access_token":api}).text
print("\033[32;1m=>",tkk)

print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)

ktra=path.exists("ck_kpn.txt")
if ktra==True:
        #print(user)
    sua=input(f"\033[37;1mBạn có muốn sửa cookie không (y/n): \033[32;1m") 
    if sua=="y":
        os.remove("ck_kpn.txt")
        b=open('ck_kpn.txt','w')
        ck_tik=input("\033[37;1mNhập cookie: \033[32;1m")
        b.write(ck_tik)
        b.close()
    else:
        b=open('ck_kpn.txt','r')
        list = b.read().splitlines()
else:
    b=open('ck_kpn.txt','w')
    ck_tik=input("\033[37;1mNhập cookie: \033[32;1m")
    b.write(ck_tik)
    b.close()

print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
delay=int(input("\033[37;1mNhập delay: \033[32;1m"))
print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)


#cau hinh
cauhinh=ss.post(f"https://tuongtaccheo.com/cauhinh/tiktok.php",headers=head).text
#cauhinhmacdinh
#chmd=cauhinh.split("Nick đang dùng: <a href='https://www.tiktok.com/@")[1].split("?'>")[0]
#print("\033[37;1mCấu hình đang chạy\033[32;1m",chmd)
#cauhinhcanchay
def ch(ck_tik,head_chh):
    try: 
        a=ss.get('https://www.tiktok.com/passport/web/account/info/?aid=1459&app_language=vi-VN&app_name=tiktok_web&battery_info=0.48&browser_language=vi-VN&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20armv8l&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F86.0.4240.198%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_id=7086378675985974827&device_platform=web_pc&focus_state=true&from_page=video&history_len=1&is_fullscreen=false&is_page_visible=true&os=windows&priority_region=VN&referer=&region=VN&screen_height=780&screen_width=360&tz_name=Asia%2FSaigon&verifyFp=verify_0c253cb955b80adc6d83ca7715c47138&webcast_language=vi-VN',headers=head_chh).json()
        name=a['data']['user_id']
        ten=a['data']['username']

        datch=ss.post(f"https://tuongtaccheo.com/cauhinh/datnick.php",headers=head,data={'iddat[]': ten, 'loai': "tt"}).text
        if datch=="1":
            #print("\033[37;1mĐặt cấu hình\033[32;1m",ten,"\033[32;1mthành công")
            return ten
        else:
            print("\033[37;1mĐặt cấu hình\033[32;1m",ten,"\033[32;1mthất bại")
            print(datch)
            return False
    except:
        return False

sleep(1)
os.system("clear")
jobtym=[]
jobfl=[]
h=0


with open('ck_kpn.txt') as f:
    size=len([0 for _ in f])
    soacc=int(size)



def nhan(id):
    caidat=ss.get("https://tuongtaccheo.com/caidat/",headers=head).text
    sodu=caidat.split('id="soduchinh">')[1].split('</strong> XU')[0]

    print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)

    nhan=ss.post('https://tuongtaccheo.com/tiktok/kiemtien/nhantien.php', headers=head, data={"id": id}).json()
    if "mess" in nhan:
        print(f"\033[37;1m=> {nhan['mess']} <> {sodu}")
    else:
        print(f"\033[37;1m{nhan}")

b=open('ck_kpn.txt','r')
list = b.read().splitlines()

while True:
    for ck_tik in list:

        head_chh= {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': ck_tik,
        'Origin': 'https://www.tiktok.com',
        'Referer': 'https://www.tiktok.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'content-type': 'application/x-www-form-urlencoded',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        }


        cauhinh=ch(ck_tik,head_chh)
        if cauhinh==False:
            continue

        get_fl=ss.get(f"https://tuongtaccheo.com/tiktok/kiemtien/getpost.php",headers=head).json()
        job=len(get_fl)

        if len(get_fl)!=0:
            print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
            print(f"\033[37;1m[\033[32;1m{cauhinh}\033[37;1m]".center(60))
            print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
            for x in get_fl:
                id = x['idpost']
                user = x['link']
                h+=1
                time = datetime.now().strftime("%H:%M:%S")
                print(f"\033[37;1m[\033[32;1m{h}\033[37;1m][\033[32;1m{time}\033[37;1m][\033[32;1mSUCCESS\033[37;1m][\033[32;1mTYM\033[37;1m][\033[32;1m{id}\033[37;1m][\033[32;1m{len(jobfl)}\033[37;1m]")
                jobfl.append(id)
                #os.system(f'xdg-open {link}')
                tym=ss.get(f"https://fireender.tk/like-tt.php?id={id}&cookie={ck_tik}")
                for i in range(delay, 0, -1):
                    print(f'\033[1;95m[KPNTOOL] Vui Lòng Đợi {i} _         ', end='\r')
                    sleep(0.25)
                    print(f'\033[1;94m[KPNTOOL] Vui Lòng Đợi {i} __        ', end='\r')
                    sleep(0.25)
                    print(f'\033[1;93m[KPNTOOL] Vui Lòng Đợi {i} ___       ', end='\r')
                    sleep(0.25)
                    print(f'\033[1;92m[KPNTOOL] Vui Lòng Đợi {i} ____      ', end='\r')
                    sleep(0.25)
                if len(jobfl)==job:
                    id=','.join(jobfl)
                    nhan(id)
                    jobfl.clear()
                    print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
                    break
        else:
            for _ in range(10,0,-1):
                print("\033[37;1mHết job đang chuyển acc khác đợi",_,end="                   \r")
                sleep(1)









