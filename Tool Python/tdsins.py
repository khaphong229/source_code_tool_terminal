import os,requests as ss
from time import sleep
import json, sys
from datetime import datetime
from os import path
import random
os.system("clear")

ktra=path.exists("api_tds.txt")
if ktra==True:
		#print(user)
	sua=input(f"Bạn có muốn sửa api không (y/n): ") 
	if sua=="y":
		os.remove("api_tds.txt")
		a=open('api_tds.txt','w')
		TDS_token=input("Nhập access token TDS: ")
		a.write(TDS_token)
		a.close()
	else:
		a=open('api_tds.txt','r')
		TDS_token=a.readline()
else:
	a=open('api_tds.txt','w')
	TDS_token=input("Nhập access token TDS: ")
	a.write(TDS_token)
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


ktra=path.exists("ins_kpn.txt")
if ktra==True:
	sua=input(f"Bạn có muốn sửa cookie không (y/n): ") 
	if sua=="y":
		os.remove("ins_kpn.txt")
		b=open('ins_kpn.txt','w')
		print("Muốn chạy đa luồng thêm cookie vô file ins_kpn.txt (mỗi dòng 1 cookie)")
		ck=input("Nhập cookie: ")
		b.write(ck)
		b.close()
	else:
		b=open('ins_kpn.txt','r')
		list = b.read().splitlines()
else:
	b=open('ins_kpn.txt','w')
	print("Muốn chạy đa luồng thêm cookie vô file ins_kpn.txt (mỗi dòng 1 cookie)")
	ck=input("Nhập cookie: ")
	b.write(ck)
	b.close()

#chon=int(input("1 <> LIKE | 2 <> FOLLOW | Bạn chọn: "))
job=int(input("Bao job thì đổi acc: "))
delay=int(input("Nhập delay: "))

os.system("clear")

#get thong tin acc


thongtinacc=ss.get(f'https://traodoisub.com/api/?fields=profile&access_token={TDS_token}').json()
print(f"{thongtinacc['data']['user']} <> {thongtinacc['data']['xu']} <> {thongtinacc['data']['xudie']}")

def check_live_user(username: str) -> bool:
    URL = "https://www.instagram.com/{}/".format(username)
    out_put = BeautifulSoup(ss.get(URL).text, "html.parser")
    meta = out_put.find("meta", property ="og:description").attrs['content']
    data = {}
    crawl = meta.split("-")[0].split(" ")
    data['Followers'] = crawl[0]
    data['Following'] = crawl[2]
    data['Posts'] = crawl[4]
    return data

#dat cau hinh
def ch(i,ck,headers):
	checkcookie = ss.get("https://www.instagram.com/", headers=headers).text
	if "Tạo một tài khoản hoặc đăng nhập Instagram" in checkcookie or "checkpoint_url" in checkcookie:
		print("Cookie Die")
		quit()

	print("-"*30)
	head = {
	'authority':'www.instagram.com',
	'cookie':ck,
	'upgrade-insecure-requests':'1',
	'sec-ch-prefers-color-scheme': 'light',
	'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': '"Windows"',
	'sec-fetch-dest': 'document',
	'sec-fetch-mode': 'navigate',
	'sec-fetch-site': 'same-origin',
	'sec-fetch-user': '?1',
	'upgrade-insecure-requests': '1',
	'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
	'viewport-width': '1366',
	}
	try:
		lay=ss.get("https://www.instagram.com/",headers=head).text
		idacc=lay.split('username')[1].split('badge_count')[0].split('\"')[2].split('\\')[0]
		#idacc= ck.split("ds_user_id=")[1].split(";")[0]

		try:
			followers, following, post = dict(check_live_user(idacc)).items()
		except:
			return False

		datch=ss.get(f'https://traodoisub.com/api/?fields=instagram_run&id={idacc}&access_token={TDS_token}').json()
		if "success" in datch:
			print(f"Acc {i} <> {idacc} <> {datch['data']['msg']}")
		else:
			print(datch['error'])
			quit()

		print("-"*30)
	except:
		return False


def likeIG(link,headers,head_a):
    try:
        post = ss.get(link + "/", headers=head_a).text
        id=post.split('{"media_id":"')[1].split('"')[0]
        like = ss.post("https://www.instagram.com/web/likes/"+id+"/like/", data="", headers=headers).text
        if '{"status":"ok"}' in like:
            return True
        elif '"spam":true' in like:
            return False
        else:
            return "notblock"
    except:
        return "wait"

def followIG(link,headers,head_a):
    try:
        un=link.split('https://www.instagram.com/')[1]
        id=ss.get(f'https://i.instagram.com/api/v1/users/web_profile_info/?username={un}',headers=headers).json()['data']['user']['id']
        follow = ss.post("https://www.instagram.com/web/friendships/"+id+"/follow/", data="", headers=headers).text
        if '{"result":"following","status":"ok"}' in follow or '{"result":"requested","status":"ok"}' in follow:
            return True
        elif '"spam":true' in follow:
            return False
        elif  "Please wait a few minutes before you try again." in follow:
            return "wait"
    except:
        return "wait"




with open('ins_kpn.txt') as f:
    size=len([0 for _ in f])
    soacc=int(size)
h=0

while True:
	for i in range(1,int(soacc)+1):
		c=i-1
		b=open('ins_kpn.txt','r')
		list = b.read().splitlines()
		ck=list[c]

		headers = {
		"x-ig-app-id": "1217981644879628",
		"x-asbd-id": "198387",
		# "x-ig-www-claim":self.www,
		"x-instagram-ajax": "c161aac700f",
		"accept": "*/*",
		"content-length": "0",
		"content-type": "application/x-www-form-urlencoded",
		"user-agent": ua,
		"x-csrftoken": ck.split('csrftoken=')[1].split(';')[0],
		"x-requested-with": "XMLHttpRequest",
		"cookie": ck,
		}
		head_a = {
		"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"cookie": ck,
		"sec-ch-prefers-color-scheme": "dark",
		"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
		"sec-ch-ua-mobile": "?0",
		"sec-ch-ua-platform": '"Windows"',
		"sec-fetch-dest": "document",
		"sec-fetch-mode": "navigate",
		"sec-fetch-site": "same-origin",
		"sec-fetch-user": "?1",
		"upgrade-insecure-requests": "1",
		"user-agent": ua,
		"viewport-width": "1366"
		}

		t=ch(i,ck,headers)
		if t == False:
			print(f'cookie acc {i} die')
			continue

		test_like=likeIG("https://www.instagram.com/p/Chk_ai-Jttg",headers,head_a)
		if test_like==False:
			print('Block like                             ')
			continue
		test_fl=followIG("https://www.instagram.com/nkhaphong",headers,head_a)
		if test_fl==False:
			print('Block follow                             ')
			continue

		while True:
			chon = random.randint(1,2)
			if chon==1:
				loai="LIKE"
				type="instagram_like"
				nhan_type="INS_LIKE_CACHE"
			elif chon==2:
				loai="FOLLOW"
				type="instagram_follow"
				nhan_type="INS_FOLLOW_CACHE"

			get_job=ss.get(f'https://traodoisub.com/api/?fields={type}&access_token={TDS_token}').json()
			if get_job['data']==[]:
				print("Hết job ...",end="                                  \r")
			else:	
				for x in get_job['data']:
					print(f"tìm thấy {len(get_job['data'])} job",end="                                  \r")
					try:
						h+=1
						id_job=x['id']
						link=x['link']

						sleep(1)

						if chon==1:
							check=likeIG(link,headers,head_a)
							if check == True:
								ok=0
							elif check == False:
								print('Block like                             ')
							elif check == "wait":
								print('"Vui lòng đợi một vài phút trước khi bạn thử lại. Đợi 5s"',end=" \r")
							elif check == "notblock":
								print('Chịu bỏ qua, like này bị gì',end=" \r")
						elif chon==2:
							check=followIG(link,headers,head_a)
							if check == True:
								ok=0
							elif check == False:
								print('Block follow                          ')
							elif check == "wait":
								print("Vui lòng đợi một vài phút trước khi bạn thử lại",end=" \r")

						sleep(2)

						time = datetime.now().strftime("%H:%M")

						nhan=ss.get(f'https://traodoisub.com/api/coin/?type={nhan_type}&id={id_job}&access_token={TDS_token}').json()

						if "success" in nhan:
							a=f"{h} <> {time} <> {loai} <> {link.split('https://www.instagram.com/')[1]} <> {nhan['data']['msg']} <> {nhan['data']['pending']}"
							for i in range(len(str(a))):
								sys.stdout.write(a[i])
								sys.stdout.flush()
								sleep(0.01)
							print()

						for i in range(delay, 0, -1):
							print(f'[KPNTOOL] Vui Lòng Đợi {i} _         ', end='\r')
							sleep(0.25)
							print(f'[KPNTOOL] Vui Lòng Đợi {i} __        ', end='\r')
							sleep(0.25)
							print(f'[KPNTOOL] Vui Lòng Đợi {i} ___       ', end='\r')
							sleep(0.25)
							print(f'[KPNTOOL] Vui Lòng Đợi {i} ____      ', end='\r')
					except:
						pass
			if h%job==0 and h>0:
				for _ in range(10,0,-1):
					print("Đang chuyển acc khác đợi",_,end=" \r")
					sleep(1)
				break

