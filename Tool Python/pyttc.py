import os, requests as ss
from time import sleep
import os.path
import json
from os import path
os.system("clear")

ktra=path.exists("api_kpn.txt")
if ktra==True:
		#print(user)
	sua=input(f"\033[37;1mBạn có muốn sửa api không (y/n): \033[32;1m") 
	if sua=="y":
		os.remove("api_kpn.txt")
		a=open('api_kpn.txt','w')
		api=input("\033[37;1mNhập api TTC: \033[32;1m")
		a.write(api)
		a.close()
	else:
		a=open('api_kpn.txt','r')
		api=a.readline()
else:
	a=open('api_kpn.txt','w')
	api=input("\033[37;1mNhập api TTC: \033[32;1m")
	a.write(api)
	a.close()
ktra=path.exists("ua_kpn.txt")
if ktra==True:
    c=open('ua_kpn.txt','r')
    ua=c.readline()
else:
    c=open('ua_kpn.txt','w')
    ua=input("\033[37;1mNhập user_agent: \033[32;1m")
    c.write(ua)
    c.close()

os.system("clear")

ck_ttc=ss.post("https://tuongtaccheo.com/logintoken.php",data={"access_token":api}).headers['set-cookie'].split(';')[0]
head = {
"cookie":ck_ttc,
"Host":"tuongtaccheo.com",
"x-requested-with":"XMLHttpRequest",
"user-agent":ua,
}
#lấy thông tin
print("\033[32;1mTOOL TTC TIKTOK BY KPN".center(60))
print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
tkk=ss.post(f"https://tuongtaccheo.com/logintoken.php",headers=head,data={"access_token":api}).text
print("\033[32;1m=>",tkk)

print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
#cau hinh
cauhinh=ss.post(f"https://tuongtaccheo.com/cauhinh/tiktok.php",headers=head).text
#cauhinhmacdinh
chmd=cauhinh.split("Nick đang dùng: <a href='https://www.tiktok.com/@")[1].split("?'>")[0]
print("\033[37;1mCấu hình đang chạy\033[32;1m",chmd)
#cauhinhcanchay


ktra=path.exists("ck_kpn.txt")
if ktra==True:
		#print(user)
	sua=input(f"\033[37;1mBạn có muốn sửa cookie không (y/n): \033[32;1m") 
	if sua=="y":
		os.remove("ck_kpn.txt")
		b=open('ck_kpn.txt','w')
		cookie=input("\033[37;1mNhập cookie: \033[32;1m")
		b.write(cookie)
		b.close()
	else:
		b=open('ck_kpn.txt','r')
		list = b.read().splitlines()
		cookie=list[0]
else:
	b=open('ck_kpn.txt','w')
	cookie=input("\033[37;1mNhập cookie: \033[32;1m")
	b.write(cookie)
	b.close()
	
head_chh= {
    'Accept': '*/*',
    'Accept-Language': 'vi-VN,vi;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': cookie,
    'Origin': 'https://www.tiktok.com',
    'Referer': 'https://www.tiktok.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent':ua,
    'content-type': 'application/x-www-form-urlencoded',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}


a=ss.get('https://www.tiktok.com/passport/web/account/info/?aid=1459&app_language=vi-VN&app_name=tiktok_web&battery_info=0.48&browser_language=vi-VN&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20armv8l&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F86.0.4240.198%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_id=7086378675985974827&device_platform=web_pc&focus_state=true&from_page=video&history_len=1&is_fullscreen=false&is_page_visible=true&os=windows&priority_region=VN&referer=&region=VN&screen_height=780&screen_width=360&tz_name=Asia%2FSaigon&verifyFp=verify_0c253cb955b80adc6d83ca7715c47138&webcast_language=vi-VN',headers=head_chh).json()
name=a['data']['username']
uid=a['data']['user_id']
while True:
    try:
        if name!="":
            datch=ss.post(f"https://tuongtaccheo.com/cauhinh/datnick.php",headers=head,data={'iddat[]': name, 'loai': "tt"}).text
            if datch=="1":
                print("\033[37;1mĐặt cấu hình\033[32;1m",name,"\033[32;1mthành công")
                break
            else:
                print("\033[37;1mĐặt cấu hình\033[32;1m",name,"\033[32;1mthất bại")
        else:
            print("\033[37;1mĐang chạy cấu hình mặc định\033[32;1m",chmd)
            break
    except:
        exit("Cookie sai")

print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
chon=input(f"\033[37;1m1 => Tym | 2 => Follow | Bạn chọn: \033[32;1m")
print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
delay=int(input("\033[37;1mNhập delay: \033[32;1m"))
os.system("clear")
print("\033[32;1mTOOL TTC TIKTOK BY KPN".center(60))
print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
head_x = {
        'Host':'t.tiktok.com',
        'Accept': '*/*',
        'Cookie': cookie,
        'x-secsdk-csrf-version':'1.2.7',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
        'x-secsdk-csrf-request':'1',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.tiktok.com',
        'Referer':'https://www.tiktok.com/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent':ua,
        }
head_xx = {
        'Accept': '*/*',
        'Cookie': cookie,
        'x-secsdk-csrf-version':'1.2.7',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
        'x-secsdk-csrf-request':'1',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.tiktok.com',
        'Referer':'https://www.tiktok.com/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent':ua,
        }
tt_token=cookie.split('tt_csrf_token=')[1].split(';')[0]
if chon=="2":
    xtoken=ss.head(f"https://t.tiktok.com/api/commit/follow/user/",headers=head_x).headers['X-Ware-Csrf-Token'].split('0,')[1].split(',')[0]
h=0
if chon=="2":
    head_fl = {
        'Content-Length': '0',
        'Host': 't.tiktok.com',
        'tt-csrf-token': tt_token,
        'x-secsdk-csrf-token': xtoken,
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': cookie,
        'Origin': 'https://www.tiktok.com',
        'Referer': 'https://www.tiktok.com/@trunj_2007',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': ua,
        'content-type': 'application/x-www-form-urlencoded',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
head_e= {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': cookie,
        'Origin': 'https://www.tiktok.com',
        'Referer': 'https://www.tiktok.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent':ua,
        'content-type': 'application/x-www-form-urlencoded',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
    }
#tym
def tym(cookie,link):
	head_a = {
	'Host':'api-kpb.tk',
	'User-Agent':ua,
	'Accept':'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
	}
	data_tym = {'cookie':cookie,'link-video':link}
	work=ss.post('http://api-kpb.tk/api/like-tiktok.php',headers=head_a,data=data_tym).json()

def follow_tiktok(cookie,linkuser):
	head_b = {
	'Host':'api-kpb.tk',
	'User-Agent':ua,
	'Accept':'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
	}
	data_fl = {'cookie':cookie,'link-user':linkuser}
	lam=ss.post('http://api-kpb.tk/api/follow-tiktok.php',headers=head_b,data=data_fl).json()
	print(lam)


def nhantym(id):
	print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
	nhan=ss.post('https://tuongtaccheo.com/tiktok/kiemtien/nhantien.php', headers=head, data={"id": id}).json()
	print("\033[37;1m=>",nhan)
	print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)

if chon=="1":
    while True:
        while True:
            idp=""
            get_tym=ss.get(f"https://tuongtaccheo.com/tiktok/kiemtien/getpost.php",headers=head).json()
            if get_tym==[]:
                print("Hết job ...",end=" \r")
                break
            else:
                for x in get_tym:
                    id = x['idpost']
                    link = x['link']
                    h+=1
                    print(f"\033[37;1m{h} • TYM • \033[32;1m",link)
                    idp+=id+","
                    #os.system(f'xdg-open {link}')
                    tym=ss.get(f"https://fireender.tk/like-tt.php?id={id}&cookie={cookie}")
                    for _ in range(delay,0,-1):
                        print("                        ",end=" \r")
                        sleep(0.25)
                        print("Chờ",end=" \r")
                        sleep(0.25)
                        print("Chờ",_,end=" \r")
                        sleep(0.25)
                        print("Chờ",_,"giây",end=" \r")
                        sleep(0.25)
                    ss.get("https://tuongtaccheo.com/refresh.php",headers=head)
                    if h%10==0:
                        nhantym(idp[:-1])

def nhan(ida):
    print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
    nhan=ss.post('https://tuongtaccheo.com/tiktok/kiemtien/subcheo/nhantien.php', headers=head, data={"id": ida}).json()
    print("\033[37;1m=>",nhan)
    print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)

if chon=="2":
    while True:
        while True:
                ida=""
                get_fl=ss.get(f"https://tuongtaccheo.com/tiktok/kiemtien/subcheo/getpost.php",headers=head).json()
                if get_fl==[]:
                    print("Hết job ...",end=" \r")
                    break
                else:
                    for x in get_fl:
                        id = x['idpost']
                        user = x['link']
                        h+=1
                        link=f"https://www.tiktok.com/@{user}"
                        print(f"\033[37;1m{h} • FOLLOW • \033[32;1m",link)
                        ida+=id+","
                        #follow_tiktok(cookie,link)
                        a=ss.get(f"https://www.tiktok.com/api/user/detail/?aid=1988&app_language=vi-VN&app_name=tiktok_web&battery_info=1&browser_language=vi&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%206.1%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F102.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_id=7111522143247074818&device_platform=web_pc&focus_state=true&from_page=user&history_len=17&is_fullscreen=false&is_page_visible=true&language=vi-VN&os=windows&priority_region=VN&referer=&region=VN&screen_height=768&screen_width=1366&secUid=&tz_name=Asia%2FBangkok&uniqueId={user}&webcast_language=vi-VN",headers=head_e).json()
                        try:
                            user_id=a['userInfo']['user']['id']
                            sec_id=a['userInfo']['user']['secUid']

                        except:
                            pass
                        else:
                            fl = ss.post(f'https://t.tiktok.com/api/commit/follow/user/?aid=1988&app_language=vi-VN&app_name=tiktok_web&battery_info=1&browser_language=vi&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%206.1%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F102.0.0.0%20Safari%2F537.36&channel=tiktok_web&channel_id=0&cookie_enabled=true&device_id={uid}&device_platform=web_pc&focus_state=true&from=18&fromWeb=1&from_page=user&from_pre=0&history_len=3&is_fullscreen=false&is_page_visible=true&os=windows&priority_region=VN&referer=&region=VN&screen_height=768&screen_width=1366&sec_user_id={sec_id}&type=1&tz_name=Asia%2FBangkok&user_id={user_id}&webcast_language=vi-VN', headers=head_fl).text
                        for _ in range(delay,0,-1):
                            print("                        ",end=" \r")
                            sleep(0.25)
                            print("Chờ",end=" \r")
                            sleep(0.25)
                            print("Chờ",_,end=" \r")
                            sleep(0.25)
                            print("Chờ",_,"giây",end=" \r")
                            sleep(0.25)
                        ss.get("https://tuongtaccheo.com/refresh.php",headers=head)
                        if h%10==0:
                            nhan(ida[:-1])








