import os, requests as ss
from time import sleep
from datetime import datetime
from os import path
from bs4 import BeautifulSoup

ktra=path.exists("ck_hust.txt")
if ktra==True:
		#print(user)
	sua=input(f"\033[37;1mBạn có muốn sửa cookie không (y/n): \033[32;1m") 
	if sua=="y":
		os.remove("ck_hust.txt")
		a=open('ck_hust.txt','w')
		ck=input("Nhập cookie web: ")
		a.write(ck)
		a.close()
	else:
		a=open('ck_hust.txt','r')
		ck=a.readline()
else:
	a=open('ck_hust.txt','w')
	ck=input("Nhập cookie web: ")
	a.write(ck)
	a.close()

print("1 <> Tiktok")
print("2 <> Instagram")
print("3 <> Instagram đa luồng")
chon=int(input("Bạn chọn: "))

if chon ==2:
	#cookie=input("Nhập cookie ins: ")
	ktra=path.exists("hustins.txt")
	if ktra==True:
	        #print(user)
	    sua=input(f"\033[37;1mBạn có muốn sửa cookie không (y/n): \033[32;1m") 
	    if sua=="y":
	        os.remove("hustins.txt")
	        b=open('hustins.txt','w')
	        cookie=input("\033[37;1mNhập cookie: \033[32;1m")
	        b.write(cookie)
	        b.close()
	    else:
	        b=open('hustins.txt','r')
	        cookie=b.readline()
	else:
	    b=open('hustins.txt','w')
	    cookie=input("\033[37;1mNhập cookie: \033[32;1m")
	    b.write(cookie)
	    b.close()



delay=int(input("Nhập delay: "))

os.system("clear")



head={
	"host":"hust.media",
	"upgrade-insecure-requests": "1",
	"cookie":ck,
}



def thanh():
	print("\033[37;1m---"*15)


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

def followIG(id,headers):
    try:
        #un=link.split('https://www.instagram.com/')[1]
        #id=ss.get(f'https://i.instagram.com/api/v1/users/web_profile_info/?username={user}',headers=headers).json()['data']['user']['id']
        follow = ss.post("https://www.instagram.com/web/friendships/"+id+"/follow/", data="", headers=headers).text
        if '{"result":"following","status":"ok"}' in follow or '{"result":"requested","status":"ok"}' in follow:
            return True
        elif '"spam":true' in follow:
            return False
        elif  "Please wait a few minutes before you try again." in follow:
            return "wait"
    except:
        return "wait"


thong_tin=ss.get("https://hust.media/",headers=head).text
ten=thong_tin.split('<h6 class="mb-0">')[1].split('</h6>')[0]
xu=thong_tin.split('#fec8c3;">')[1].split('</')[0]
print(f"\033[32;1m{ten} \033[37;1m<> \033[32;1m{xu}")

thanh()
h=0
if chon==1:
	pro=ss.get("https://hust.media/profile/",headers=head).text
	tk=pro.split('Tk làm nhiệm vụ @')[1].split(' <a')[0]
	key=pro.split('<input type="text" id="input-api" class="form-control form-control-alternative" value="')[1].split('"')[0]

	print(f"\033[32;1mĐang chạy acc tiktok \033[37;1m{tk}")

	thanh()

	while True:
		try:
			job=ss.get("https://hust.media/followtiktok.php",headers=head).text

			#key=job.split('"key": "')[1].split('",')[0]
			id=job.split("var url = '")[1].split("'")[0]

			sodu=job.split("animateNumber(")[2].split(",")[0]
			h+=1
			time = datetime.now().strftime("%H:%M:%S")
			print(f"\033[37;1m[\033[32;1m{h}\033[37;1m][\033[32;1m{time}\033[37;1m][\033[32;1m{id}\033[37;1m]")

			if "video" in id:
				idd=id.split("video/")[1]
				#print(idd)
				#tym=ss.get(f"https://fireender.tk/like-tt.php?id={idd}&cookie={ck_tik}")
				os.system(f'xdg-open {id}')
				# os.system(f'cmd /c start {id}')
				for i in range(delay, 0, -1):
					print(f'\033[1;95m[KPNTOOL] Vui Lòng Đợi {i} _         ', end='\r')
					sleep(0.25)
					print(f'\033[1;94m[KPNTOOL] Vui Lòng Đợi {i} __        ', end='\r')
					sleep(0.25)
					print(f'\033[1;93m[KPNTOOL] Vui Lòng Đợi {i} ___       ', end='\r')
					sleep(0.25)
					print(f'\033[1;92m[KPNTOOL] Vui Lòng Đợi {i} ____      ', end='\r')
				nhan=ss.post("https://hust.media/checktim.php",headers=head,data=f"key={key}&action=add&service=follow&link={id}").json()

				try:
					if "Nhận" in nhan['order']:
						thanh()
						print(f"\033[37;1m[\033[32;1m{nhan['order']}\033[37;1m][\033[32;1m{sodu}\033[37;1m]")
						thanh()
				except:
					thanh()
					print(nhan['error'])
					thanh()

			else:
				link=job.split('<a onclick="loading()" href="')[1].split('" target="_blank"')[0]

				os.system(f'xdg-open {link}')
				# os.system(f'cmd /c start {link}')
				for i in range(delay, 0, -1):
					print(f'\033[1;95m[KPNTOOL] Vui Lòng Đợi {i} _         ', end='\r')
					sleep(0.25)
					print(f'\033[1;94m[KPNTOOL] Vui Lòng Đợi {i} __        ', end='\r')
					sleep(0.25)
					print(f'\033[1;93m[KPNTOOL] Vui Lòng Đợi {i} ___       ', end='\r')
					sleep(0.25)
					print(f'\033[1;92m[KPNTOOL] Vui Lòng Đợi {i} ____      ', end='\r')
				nhan=ss.post("https://hust.media/checktiktok.php",headers=head,data=f"key={key}&action=add&service=follow&link={id}").json()

				try:
					if "Nhận" in nhan['order']:
						thanh()
						print(f"\033[37;1m[\033[32;1m{nhan['order']}\033[37;1m][\033[32;1m{sodu}\033[37;1m]")
						thanh()
				except:
					thanh()
					print(nhan['error'])
					thanh()

		except:
			continue


elif chon==2:

	headers = {
		"x-ig-app-id": "1217981644879628",
		"x-asbd-id": "198387",
		# "x-ig-www-claim":self.www,
		"x-instagram-ajax": "c161aac700f",
		"accept": "*/*",
		"content-length": "0",
		"content-type": "application/x-www-form-urlencoded",
		"x-csrftoken": cookie.split('csrftoken=')[1].split(';')[0],
		"x-requested-with": "XMLHttpRequest",
		"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
		"cookie": cookie,
		}

	pro=ss.get("https://hust.media/profile/",headers=head).text
	key=pro.split('<input type="text" id="input-api" class="form-control form-control-alternative" value="')[1].split('"')[0]



	def cauhinh(cookie):
		head_a= {
		'authority':'www.instagram.com',
		'cookie':cookie,
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

		head_ch={
			"Host":"hust.media",
			"content-length":"67",
			"origin":"https://hust.media",
			"content-type":"application/x-www-form-urlencoded",
			"upgrade-insecure-requests": "1",
			"referer":"https://hust.media/dangky2.php",
			"cookie":ck,
			"user-agent":"Mozilla/5.0 (Linux; Android 10; Active 3 Build/QP1A.190711.020;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36",
		}

		checkcookie = ss.get("https://www.instagram.com/", headers=headers).text
		if "Tạo một tài khoản hoặc đăng nhập Instagram" in checkcookie or "checkpoint_url" in checkcookie:
			print("Cookie Die")
			quit()
		try:
			lay=ss.get("https://www.instagram.com/",headers=head_a).text
			idacc=lay.split('username')[1].split('badge_count')[0].split('\"')[2].split('\\')[0]


			followers, following, post = dict(check_live_user(idacc)).items()

			dat=ss.post("https://hust.media/dangky2.php", headers=head_ch,data=f"username={idacc}&submit=",timeout=None)

			return idacc
		except:
			return False

	ktra=cauhinh(cookie)

	a=ss.get("https://hust.media/cheoig.php",headers=head).text
	accchay=a.split('<a href="https://www.tiktok.com/@')[1].split('">')[0]

	if ktra!=accchay or ktra==False:
		print(f"Đặt cấu hình {ktra} thất bại")
		quit()

	print(f"\033[37;1m[\033[32;1m{accchay}\033[37;1m]".center(60))
	thanh()

	while True:
		try:
			job=ss.get("https://hust.media/cheoig.php",headers=head).text
			id=job.split("var url = '")[1].split("'")[0]
			sodu=job.split("animateNumber(")[2].split(",")[0]
			user=job.split('<h2 class="mb-0"><i class="ni ni-shop"></i> ')[1].split('</h2>')[0].split(' <')[0]
			h+=1

			time = datetime.now().strftime("%H:%M:%S")
			print(f"\033[37;1m[\033[32;1m{h}\033[37;1m][\033[32;1m{time}\033[37;1m][\033[32;1mSUCCESS\033[37;1m][\033[32;1m{id}\033[37;1m][\033[32;1m{user}\033[37;1m]")

			check=followIG(id,headers)
			if check == True:
				ok=0
			elif check == False:
				print('Block follow                          ')
			elif check == "wait":
				print("Đợi vài phút trước khi thử lại",end=" \r")

			for i in range(delay, 0, -1):
				print(f'\033[1;95m[KPNTOOL] Vui Lòng Đợi {i} _         ', end='\r')
				sleep(0.25)
				print(f'\033[1;94m[KPNTOOL] Vui Lòng Đợi {i} __        ', end='\r')
				sleep(0.25)
				print(f'\033[1;93m[KPNTOOL] Vui Lòng Đợi {i} ___       ', end='\r')
				sleep(0.25)
				print(f'\033[1;92m[KPNTOOL] Vui Lòng Đợi {i} ____      ', end='\r')

			nhan=ss.post("https://hust.media/checkig.php",headers=head,data=f"key={key}&action=add&service=follow&link={id}").json()
			try:
				if "Nhận" in nhan['order']:
					thanh()
					print(f"\033[37;1m[\033[32;1m{nhan['order']}\033[37;1m][\033[32;1m{sodu}\033[37;1m]")
					thanh()
			except:
				thanh()
				print(nhan['error'])
				thanh()
				continue
		except:
			continue



else:
	loi=[]
	ds=[]
	kt=path.exists("hustins_dl.txt")
	if kt==False:
		g=open('hustins_dl.txt','w')
		print("Đã tạo file chứa cookie instagram")
		print("Vui lòng vô file hustins_dl.txt thêm cookie")
		print("Lưu ý: Mỗi cookie / 1 dòng")
		quit()

	sojob=int(input("Nhận thành công bao nhiêu lần thì đổi acc: "))
	soloi=int(input("Lỗi bao nhiêu lần thì đổi acc: "))
	thanh()

	b=open('hustins_dl.txt','r')
	list = b.read().splitlines()



	pro=ss.get("https://hust.media/profile/",headers=head).text
	key=pro.split('<input type="text" id="input-api" class="form-control form-control-alternative" value="')[1].split('"')[0]

	while True:

		for cookie in list:


			headers = {
			"x-ig-app-id": "1217981644879628",
			"x-asbd-id": "198387",
			# "x-ig-www-claim":self.www,
			"x-instagram-ajax": "c161aac700f",
			"accept": "*/*",
			"content-length": "0",
			"content-type": "application/x-www-form-urlencoded",
			"x-csrftoken": cookie.split('csrftoken=')[1].split(';')[0],
			"x-requested-with": "XMLHttpRequest",
			"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
			"cookie": cookie,
			}

			head_a= {
			'authority':'www.instagram.com',
			'cookie':cookie,
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
			head_ch={
				"Host":"hust.media",
				"content-length":"67",
				"origin":"https://hust.media",
				"content-type":"application/x-www-form-urlencoded",
				"upgrade-insecure-requests": "1",
				"referer":"https://hust.media/dangky2.php",
				"cookie":ck,
				"user-agent":"Mozilla/5.0 (Linux; Android 10; Active 3 Build/QP1A.190711.020;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36",
			}


			def cauhinh():
				checkcookie = ss.get("https://www.instagram.com/", headers=headers).text
				if "Tạo một tài khoản hoặc đăng nhập Instagram" in checkcookie or "checkpoint_url" in checkcookie:
					print("Cookie Die")
					
					return False
				try:

					lay=ss.get("https://www.instagram.com/",headers=head_a).text
					idacc=lay.split('username')[1].split('badge_count')[0].split('\"')[2].split('\\')[0]

					try:
						followers, following, post = dict(check_live_user(idacc)).items()
					except:
						return False

					dat=ss.post("https://hust.media/dangky2.php", headers=head_ch,data=f"username={idacc}&submit=", timeout=None)
					

					return idacc
				except:
					return False

			while True:
				ktra=cauhinh()

				if ktra==False or ktra=="page_logging":
					break

				try:
					a=ss.get("https://hust.media/cheoig.php",headers=head).text
					accchay=a.split('<a href="https://www.tiktok.com/@')[1].split('">')[0]
				except:
					break

				if ktra!=accchay:
					print(f"Đặt cấu hình {ktra} thất bại")
					for _ in range(60,0,-1):
						print("\033[37;1mĐang chuyển acc",_,end="                   \r")
						sleep(1)
					#continue
				else:
					break

			thanh()
			print(f"\033[37;1m[\033[32;1m{accchay}\033[37;1m]".center(60))
			thanh()
			thanh()

			while True:
				try:
					job=ss.get("https://hust.media/cheoig.php",headers=head).text
					id=job.split("var url = '")[1].split("'")[0]
					sodu=job.split("animateNumber(")[2].split(",")[0]
					user=job.split('<h2 class="mb-0"><i class="ni ni-shop"></i> ')[1].split('</h2>')[0].split(' <')[0]
					h+=1


					time = datetime.now().strftime("%H:%M:%S")
					print(f"\033[37;1m[\033[32;1m{h}\033[37;1m][\033[32;1m{time}\033[37;1m][\033[32;1mSUCCESS\033[37;1m][\033[32;1m{id}\033[37;1m][\033[32;1m{user}\033[37;1m]")

					check=followIG(id,headers)
					if check == True:
						ok=0
					elif check == False:
						print('Block follow                          ')
						break
					elif check == "wait":
						print("Đợi vài phút trước khi thử lại",end=" \r")

					for i in range(delay, 0, -1):
						print(f'\033[1;95m[KPNTOOL] Vui Lòng Đợi {i} _         ', end='\r')
						sleep(0.25)
						print(f'\033[1;94m[KPNTOOL] Vui Lòng Đợi {i} __        ', end='\r')
						sleep(0.25)
						print(f'\033[1;93m[KPNTOOL] Vui Lòng Đợi {i} ___       ', end='\r')
						sleep(0.25)
						print(f'\033[1;92m[KPNTOOL] Vui Lòng Đợi {i} ____      ', end='\r')

					nhan=ss.post("https://hust.media/checkig.php",headers=head,data=f"key={key}&action=add&service=follow&link={id}").json()
					try:
						if "Nhận" in nhan['order']:
							thanh()
							print(f"\033[37;1m[\033[32;1m{nhan['order']}\033[37;1m][\033[32;1m{sodu}\033[37;1m]")
							thanh()
							ds.append(nhan['order'])
					except:
						thanh()
						print(nhan['error'])
						loi.append(nhan['error'])
						thanh()
						#if "Bạn chưa theo dõi nick nào, hãy theo dõi khi nhận xu" in nhan['error'] or "Kiểm tra lại nick đang chạy!" in nhan['error'] or "Đã xảy ra lỗi vui lòng ib ad" in nhan['error']:
						if len(loi)==soloi:
							loi.clear()
							ds.clear()
							for _ in range(60,0,-1):
								print("\033[37;1mĐang chuyển acc",_,end="                   \r")
								sleep(1)
							break

					if len(ds)==sojob:
						ds.clear()
						for _ in range(60,0,-1):
							print("\033[37;1mĐang chuyển acc",_,end="                   \r")
							sleep(1)
						break		
				except:
					continue