import os, requests as ss
from time import sleep
import os.path
import json
from os import path
from datetime import datetime
os.system("clear")
ktra=path.exists("api_tds.txt")
if ktra==True:
		#print(user)
	sua=input(f"\033[37;1mBạn có muốn sửa access token không (y/n): \033[32;1m") 
	if sua=="y":
		os.remove("api_tds.txt")
		a=open('api_tds.txt','w')
		api=input("\033[37;1mNhập access token TDS: \033[32;1m")
		a.write(api)
		a.close()
	else:
		a=open('api_tds.txt','r')
		api=a.readline()
else:
	a=open('api_tds.txt','w')
	api=input("\033[37;1mNhập access token TDS: \033[32;1m")
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

head = {
"host":"traodoisub.com",
"content-type":"application/x-www-form-urlencoded; charset=UTF-8",
"user-agent":ua,
}

os.system("clear")

print("\033[32;1mTOOL TDS TIKTOK BY KPN".center(60))
print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)

ktra=path.exists("ck_kpn.txt")
if ktra==True:

    sua=input(f"\033[37;1mBạn có muốn sửa cookie không (y/n): \033[32;1m") 
    if sua=="y":
        f=open("ck_kpn.txt","w")
        soacc = int(input("Nhập số acc muốn chạy: "))

        for a in range(soacc):
            print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
            f.write(input(f"\033[33;1mNhap cookie cho acc {a+1}:")+"\n")
            print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
        f.close()
    else:
        b=open('ck_kpn.txt','r')
        list = b.read().splitlines()
else:

    f=open("ck_kpn.txt","w")
    soacc = int(input("Nhập số acc muốn chạy: "))

    for a in range(soacc):
        print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
        f.write(input(f"\033[33;1mNhap cookie cho acc {a+1}:")+"\n")
        print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
    f.close()

def cauhinh(cookie,api):
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
    name=a['data']['user_id']
    ten=a['data']['username']
    datch=ss.get(f"https://traodoisub.com/api/?fields=tiktok_run&id={name}&access_token={api}",headers=head).json()
    if "success" in datch:
        return ten
    else:
        print(f"Thêm acc {ten} vào cấu hình đi")
        return False
        


delay=int(input("\033[37;1mNhập delay: \033[32;1m"))
os.system("clear")
print("\033[32;1mTOOL TDS TIKTOK BY KPN".center(60))
print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
thongtin=ss.get(f"https://traodoisub.com/api/?fields=profile&access_token={api}").json()
if "success" in thongtin:
	print(f"\033[32;1mTài khoản {thongtin['data']['user']} \033[36;1m<> \033[32;1m{thongtin['data']['xu']} xu")
else:
	print("Token tds sai rồi")
	quit()

h=0



b=open('ck_kpn.txt','r')
list = b.read().splitlines()


def nhan(api):
	nhan=ss.get(f'https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW&id=TIKTOK_FOLLOW_API&access_token={api}').json()
	print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
	if "success" in nhan:
		print(f"\033[36;1mNhận thành công {nhan['data']['msg']} <> {nhan['data']['xu']}")
	if "error" in nhan:
		print(f"\033[37;1m[\033[31;1m{nhan['error']}\033[37;1m]")
	print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)

while True:
    for cookie in list:
        for _ in range(5,0,-1):
            print("\033[37;1mĐang tải job",_,end="                   \r")
            sleep(1)
        dat=cauhinh(cookie,api)
        print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
        print(f"\033[37;1m[\033[32;1m{dat}\033[37;1m]".center(60))
        print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
        if dat==False:
            quit()
        while True:
            get_cmt=ss.get(f"https://traodoisub.com/api/?fields=tiktok_follow&access_token={api}",headers=head).json()
            
            if get_cmt['data']!=[]:

                #print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
                #print(f"\033[37;1m[\033[32;1m{dat}\033[37;1m]".center(60))
                #print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
                for x in get_cmt['data']:
                    idjob = x['id']
                    id=x['real_id']
                    uid = x['uniqueID']

                    h+=1
                    time = datetime.now().strftime("%H:%M:%S")
                    #print(f"\033[37;1m[\033[32;1m{h}\033[37;1m][\033[32;1m{time}\033[37;1m][\033[32;1mSUCCESS\033[37;1m][\033[32;1mFOLLOW\033[37;1m][\033[32;1m{id}\033[37;1m][\033[32;1m{uid}\033[37;1m]")

                    head_tik={
                    "Host":"api16-normal-c-useast2a.tiktokv.com",
                    "Cookie":cookie,
                    }

                    fll= ss.get(f"https://api16-normal-c-useast2a.tiktokv.com/aweme/v1/commit/follow/user/?user_id={id}&type=1&aid=385522",headers=head_tik).json()

                    for i in range(delay, 0, -1):
                        print(f'\033[1;95m[KPNTOOL] Vui Lòng Đợi {i} _         ', end='\r')
                        sleep(0.25)
                        print(f'\033[1;94m[KPNTOOL] Vui Lòng Đợi {i} __        ', end='\r')
                        sleep(0.25)
                        print(f'\033[1;93m[KPNTOOL] Vui Lòng Đợi {i} ___       ', end='\r')
                        sleep(0.25)
                        print(f'\033[1;92m[KPNTOOL] Vui Lòng Đợi {i} ____      ', end='\r')
                        sleep(0.25)

                    duyet=ss.get(f'https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW_CACHE&id={idjob}&access_token={api}').json()

                    print(f"\033[37;1m[\033[32;1m{h}\033[37;1m][\033[32;1m{time}\033[37;1m][\033[32;1mSUCCESS\033[37;1m][\033[32;1mFOLLOW\033[37;1m][\033[32;1m{id}\033[37;1m][\033[32;1m{uid}\033[37;1m][\033[32;1m{duyet['cache']}\033[37;1m]")

                if duyet['cache'] > 9:
                    nhan(api)
                    break
            else:
                #for _ in range(10,0,-1):
                    #print("\033[37;1mHết job đang chuyển acc khác đợi",_,end="                   \r")
                    #sleep(1)
                print("\033[37;1mHết job rồi",end="                   \r")















