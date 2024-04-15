import os, requests as ss
from time import sleep
import os.path
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
#cau hinh
cauhinh=ss.post(f"https://tuongtaccheo.com/cauhinh/tiktok.php",headers=head).text
#cauhinhmacdinh
chmd=cauhinh.split("Nick đang dùng: <a href='https://www.tiktok.com/@")[1].split("?'>")[0]
print("\033[37;1mCấu hình đang chạy\033[32;1m",chmd)
#cauhinhcanchay
ktra=path.exists("ck_daluong_kpn.txt")
if ktra==False:
	b=open('ck_daluong_kpn.txt','w')
	b.close()

with open('ck_daluong_kpn.txt') as f:
    list_ck = f.read().splitlines()


def cauhinh(cookie):
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
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
    }

    a=ss.get("https://www.tiktok.com/vi-VN/",headers=head_chh).text
    name=a.split('"uniqueId":"')[1].split('","createTime":"0"')[0]

    while True:
        if name!="":
            datch=ss.post(f"https://tuongtaccheo.com/cauhinh/datnick.php",headers=head,data={'iddat[]': name, 'loai': "tt"}).text
            if datch!="1":
                exit("\033[37;1mĐặt cấu hình\033[32;1m",id,"\033[32;1mthất bại vui lòng thêm acc vào cấu hình")
            else:
                break
        else:
            print("\033[37;1mĐang chạy cấu hình mặc định\033[32;1m",chmd)
            break
def ten(cookie):
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
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
    }

    a=ss.get("https://www.tiktok.com/vi-VN/",headers=head_chh).text
    name=a.split('"uniqueId":"')[1].split('","createTime":"0"')[0]
    return name

print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
chon=input(f"\033[37;1m1 => Tym | 2 => Follow | Bạn chọn: \033[32;1m")
print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
delay=int(input("\033[37;1mNhập delay: \033[32;1m"))
os.system("clear")
print("\033[32;1mTOOL TTC TIKTOK BY KPN".center(60))
print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)

h=0
def fl(cookie):
    head_fl = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': cookie,
        'Origin': 'https://www.tiktok.com',
        'Referer': 'https://www.tiktok.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
    }
    response = ss.get(url=link,headers=head_fl).text
    return response
#tym
def tym(cookie,link):
	head_a = {
	'Host':'api-kpb.tk',
	'User-Agent':'Mozilla/5.0 (Linux; Android 9; RMX1811) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
	'Accept':'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
	}
	data_tym = {'cookie':cookie,'link-video':link}
	work=ss.post('http://api-kpb.tk/api/like-tiktok.php',headers=head_a,data=data_tym).json()

def nhantym(id):
	print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
	nhan=ss.post('https://tuongtaccheo.com/tiktok/kiemtien/nhantien.php', headers=head, data={"id": id}).json()
	print("\033[37;1m=>",nhan)
	print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
if chon=="1":
    while True:
        for cookie in list_ck:
                cauhinh(cookie)
            #while True:
                idp=""
                get_tym=ss.get(f"https://tuongtaccheo.com/tiktok/kiemtien/getpost.php",headers=head).json()
                if get_tym==[]:
                    print("Hết job ...",end=" \r")
                    if len(idp)>160:
                        nhantym(idp[:-1])
                    break
                else:
                    print(f"\033[33;1m[{ten(cookie)}]".center(60))
                    for x in get_tym:
                        id = x['idpost']
                        link = x['link']
                        h+=1
                        #print(f"\033[33;1m[{ten(cookie)}]".center(60))
                        try:
                            print(f"\033[37;1m{h} • TYM • \033[32;1m{link}")
                        except:
                        	break
                        idp+=id+","
                        #os.system(f'xdg-open {link}')
                        tym(cookie,link)
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
                
                
                    

def nhan(id):
    print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
    nhan=ss.post('https://tuongtaccheo.com/tiktok/kiemtien/subcheo/nhantien.php', headers=head, data={"id": id}).json()
    print("\033[37;1m=>",nhan)
    print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
             
if chon=="2":
    while True:
        for cookie in list_ck:
            cauhinh(cookie)
            while True:
                    idp=""
                    get_fl=ss.get(f"https://tuongtaccheo.com/tiktok/kiemtien/subcheo/getpost.php",headers=head).json()
                    if get_fl==[]:
                        print("Hết job ...",end=" \r")
                        break
                    else:
                        #get_tym=ss.get(f"https://tuongtaccheo.com/tiktok/kiemtien/subcheo/getpost.php",headers=head).json()
                        for x in get_fl:
                            id = x['idpost']
                            user = x['link']
                            h+=1
                            link=f"https://www.tiktok.com/@{user}"
                            try:
                                print(f"\033[37;1m{h} • FOLLOW • \033[32;1m{link} • \033[37;1m{ten(cookie)}")
                            except:
                                pass
                            idp+=id+","
                            fl(cookie)
                            try:
                                user_id = response.split(',"authorId":"')[1].split('","authorSecId"')[0]
                                sec_id = response.split('"authorSecId":"')[1].split('","avatarThumb"')[0]
                                fl = ss.post(f'https://t.tiktok.com/api/commit/follow/user/?aid=1988&app_language=vi-VN&app_name=tiktok_web&battery_info=1&browser_language=vi-VN&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20x86_64&browser_version=5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F103.0.0.0%20Safari%2F537.36&channel=tiktok_web&channel_id=0&cookie_enabled=true&device_id=7110956705597228546&device_platform=web_pc&focus_state=true&from=18&fromWeb=1&from_page=user&from_pre=0&history_len=2&is_fullscreen=false&is_page_visible=true&os=linux&priority_region=VN&referer=&region=VN&screen_height=768&screen_width=1360&sec_user_id={sec_id}&type=1&tz_name=Asia%2FSaigon&user_id={user_id}&webcast_language=vi-VN', headers=head_fl).text
                            except:
                                break
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
                                nhan(idp[:-1])
                        











