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
else:
    b=open('ck_kpn.txt','w')
    cookie=input("\033[37;1mNhập cookie: \033[32;1m")
    b.write(cookie)
    b.close()
    
def cauhinh(cookie,ck_ttc,ua):
    print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
    head = {
    "cookie":ck_ttc,
    "Host":"tuongtaccheo.com",
    "x-requested-with":"XMLHttpRequest",
    "user-agent":ua,
    }
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
    try:
    	name=a['data']['username']
    except:
    	quit()
    uid=a['data']['user_id']
    while True:
        if name!="":
            datch=ss.post(f"https://tuongtaccheo.com/cauhinh/datnick.php",headers=head,data={'iddat[]': name, 'loai': "tt"}).text
            if datch=="1":
                print("\033[37;1mĐặt cấu hình\033[32;1m",name,"\033[32;1mthành công")
                print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
                break
            else:
                print("\033[37;1mĐặt cấu hình\033[32;1m",name,"\033[32;1mthất bại")
                quit()
        else:
            quit()

print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
delay=int(input("\033[37;1mNhập delay: \033[32;1m"))
os.system("clear")
print("\033[32;1mTOOL TTC TIKTOK BY KPN".center(60))
print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)


def nhan_cmt(id,loi,delay,ck_ttc,ua):
    head_tt = {
    "cookie":ck_ttc,
    "content-length":"22",
    "Host":"tuongtaccheo.com",
    "origin":"https://tuongtaccheo.com",
    "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
    "referer":"https://tuongtaccheo.com/tiktok/kiemtien/cmtcheo/",
    "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
    "x-requested-with":"XMLHttpRequest",
    "user-agent":ua,
    }
    nhan=ss.post('https://tuongtaccheo.com/tiktok/kiemtien/cmtcheo/nhantien.php', headers=head_tt, data={"id":id}).text
    for i in range(1,loi+1):
        if nhan=='{"mess":"Thành công, bạn được cộng 600 xu"}':
            print("\033[37;1m=>",nhan)
            break
        else:
            print(f"\033[37;1m[\033[31;1mLỗi nhận lần {i}\033[37;1m]",end="                                \r")
            sleep(delay)
            nhan=ss.post('https://tuongtaccheo.com/tiktok/kiemtien/cmtcheo/nhantien.php', headers=head_tt, data={"id":id}).text
            if nhan=='{"mess":"Thành công, bạn được cộng 600 xu"}':
                print("\033[37;1m=>",nhan)
                break
    print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)

h=0
with open('ck_kpn.txt') as f:
    list_ck = f.read().splitlines()


loi=int(input(f"\033[37;1mNếu nhận xu lỗi thì nhận lại mấy lần: \033[32;1m"))

while True:
    for cookie in list_ck:
        cauhinh(cookie,ck_ttc,ua)
        tt_token=cookie.split('tt_csrf_token=')[1].split(';')[0]
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
        xtoken=ss.head(f"https://www.tiktok.com/api/comment/publish/",headers=head_xx).headers['x-ware-csrf-token'].split('0,')[1].split(',')[0]
        head_cmt = {
        'authority': 'www.tiktok.com',
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': cookie,
        'origin': 'https://www.tiktok.com',
        'referer': 'https://www.tiktok.com/@toeicdoclacungsec/video/7123952252527660315',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'tt-csrf-token': tt_token,
        'user-agent': ua,
        'x-secsdk-csrf-token': xtoken,
        }
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
        g=ss.get('https://www.tiktok.com/passport/web/account/info/?aid=1459&app_language=vi-VN&app_name=tiktok_web&battery_info=0.48&browser_language=vi-VN&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20armv8l&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F86.0.4240.198%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_id=7086378675985974827&device_platform=web_pc&focus_state=true&from_page=video&history_len=1&is_fullscreen=false&is_page_visible=true&os=windows&priority_region=VN&referer=&region=VN&screen_height=780&screen_width=360&tz_name=Asia%2FSaigon&verifyFp=verify_0c253cb955b80adc6d83ca7715c47138&webcast_language=vi-VN',headers=head_chh).json()
        uid=g['data']['user_id']

        while True:
            get_cmt=ss.get(f"https://tuongtaccheo.com/tiktok/kiemtien/cmtcheo/getpost.php",headers=head).json()
            if get_cmt==[]:
                print("Hết job ...",end=" \r")
                break
            else:
                try:
                    for x in get_cmt:
                        id = x['idpost']
                        link = x['link']
                        nd=x['nd']
                        ndcmt=json.loads(nd)[0]
                        h+=1
                        print(f"\033[37;1m[\033[32;1m{h}\033[37;1m][\033[32;1mCOMMENT\033[37;1m][\033[32;1m{id}\033[37;1m]")
                        try:
                            cmt=ss.post(f"https://www.tiktok.com/api/comment/publish/?aid=1988&app_language=vi-VN&app_name=tiktok_web&aweme_id={id}&battery_info=0.48&browser_language=vi-VN&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20armv8l&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F86.0.4240.198%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_id={uid}&device_platform=web_pc&focus_state=true&from_page=video&history_len=2&is_fullscreen=false&is_page_visible=true&os=windows&priority_region=VN&referer=&region=VN&screen_height=780&screen_width=360&text={ndcmt}&text_extra=%5B%5D&tz_name=Asia%2FSaigon&webcast_language=vi-VN",headers=head_cmt).json()
                            check=cmt['status_msg']
                            print(f"\033[37;1m[\033[32;1m{ndcmt}\033[37;1m][\033[32;1m{check}\033[37;1m]")
                        except:
                            print(f"\033[37;1m[\033[32;1m{ndcmt}\033[37;1m][\033[31;1mCOMMENT ERROR\033[37;1m]")
                        for i in range(delay, 0, -1):
                            print(f'\033[1;95m[KPNTOOL] Vui Lòng Đợi {i} _         ', end='\r')
                            sleep(0.25)
                            print(f'\033[1;94m[KPNTOOL] Vui Lòng Đợi {i} __        ', end='\r')
                            sleep(0.25)
                            print(f'\033[1;93m[KPNTOOL] Vui Lòng Đợi {i} ___       ', end='\r')
                            sleep(0.25)
                            print(f'\033[1;92m[KPNTOOL] Vui Lòng Đợi {i} ____      ', end='\r')
                            sleep(0.25)
                        ss.get("https://tuongtaccheo.com/refresh.php",headers=head)
                        if "thành công" in check:
                            nhan_cmt(id,loi,delay,ck_ttc,ua)
                        else:
                            print(f"\033[37;1m[\033[31;1mCOMMENT ERROR\033[37;1m]                                  ")
                            sleep(10)
                            print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
                    for _ in range(10,0,-1):
                        print("Đang chuyển acc khác đợi",_,end=" \r")
                        sleep(1)
                    break
                except:
                    pass







