import os,requests as ss
from time import sleep
import json, sys
from datetime import datetime
from os import path
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

ktra=path.exists("fb_kpn.txt")
if ktra==True:
	sua=input(f"Bạn có muốn sửa cookie không (y/n): ") 
	if sua=="y":
		os.remove("fb_kpn.txt")
		b=open('fb_kpn.txt','w')
		print("Muốn chạy đa luồng thêm cookie vô file fb_kpn.txt (mỗi dòng 1 cookie)")
		ck=input("Nhập cookie: ")
		b.write(ck)
		b.close()
	else:
		b=open('fb_kpn.txt','r')
		list = b.read().splitlines()
else:
	b=open('fb_kpn.txt','w')
	print("Muốn chạy đa luồng thêm cookie vô file fb_kpn.txt (mỗi dòng 1 cookie)")
	ck=input("Nhập cookie: ")
	b.write(ck)
	b.close()


ktra=path.exists("ua_kpn.txt")
if ktra==True:
	c=open('ua_kpn.txt','r')
	ua=c.readline()
else:
	c=open('ua_kpn.txt','w')
	ua=input("\033[37;1mNhập user_agent: \033[32;1m")
	c.write(ua)
	c.close()

job=int(input("Bạn muốn làm bao nhiêu job thì đổi acc: "))
delay=int(input("Nhập delay: "))


os.system("clear")

#get thong tin acc
 
thongtinacc=ss.get(f'https://traodoisub.com/api/?fields=profile&access_token={TDS_token}').json()
print(f"{thongtinacc['data']['user']} <> {thongtinacc['data']['xu']} <> {thongtinacc['data']['xudie']}")



sleep(2)
#dat cau hinh
def ch(ck):
	print("-"*30)
	head = {
	"cookie":ck,
	}
	lay=ss.get("https://mbasic.facebook.com/home.php?ref_component=mbasic_home_header&ref_page=%2Fwap%2Fprofile_timeline.php&refid=17",headers=head).text
	idacc=lay.split('?av=')[1].split('&amp;')[0]

	get_name=ss.get(f'https://mbasic.facebook.com/profile.php?id={idacc}&_rdr',headers=head).text
	name=get_name.split('<head><title>')[1].split('</')[0]

	datch=ss.get(f'https://traodoisub.com/api/?fields=run&id={idacc}&access_token={TDS_token}').json()
	if "success" in datch:
		print(f"{name} <> {datch['data']['msg']}")
	else:
		print(datch)
		quit()

	print("-"*30)



def likepost(ck,id):
	head = {"cookie":ck}
	link = ss.get("https://mbasic.facebook.com/"+id,headers=head).url
	b = ss.get(link,headers=head).text
	url = "https://mbasic.facebook.com/a/like.php?"+b.split('/a/like.php?')[1].split('"')[0].replace('amp;','')
	like = ss.get(url,headers=head,allow_redirects=False).text
	if like=="":
		return True
	elif "Tài khoản của bạn hiện bị hạn chế" in like:
		return False
	else:
		return like

#get job
type="like"
h=0

with open('fb_kpn.txt') as f:
    size=len([0 for _ in f])
    soacc=int(size)

while True:
	for i in range(1,int(soacc)+1):
		c=i-1
		b=open('fb_kpn.txt','r')
		list = b.read().splitlines()
		ck=list[c]

		ch(ck)

		sleep(2)

		head_id={"content-type":"application/x-www-form-urlencoded; charset=UTF-8","Host":"id.traodoisub.com","user-agent":ua,}
		while True:
			get_job=ss.get(f'https://traodoisub.com/api/?fields={type}&access_token={TDS_token}').json()
			if "error" in get_job:
				i=int(get_job['countdown'])
				for t in range(i+60,0,-1):
					print(f"Thao tác quá nhanh đợi {t} giây",end="                             \r")
					sleep(1)
			else:
				for x in get_job:
					print(f"Đang có {len(get_job)} nhiệm vụ",end="                             \r")
					try:
						id_job=x['id']
						get_id=ss.post("https://id.traodoisub.com/api.php",headers=head_id,data=f"link=https://mbasic.facebook.com/{id_job}").json()
						id=get_id['id']

						print(f"Đang like bài {id}",end="                             \r")

						check=likepost(ck,id)

						sleep(2)

						if check==False:
							print("Tài khoản của bạn hiện bị hạn chế")
						else:

							time = datetime.now().strftime("%H:%M")
							
							h+=1
							nhan=ss.get(f'https://traodoisub.com/api/coin/?type=LIKE&id={id_job}&access_token={TDS_token}').json()
							#print(nhan)
							if "error" in nhan:
								a=f"{h} <> {time} <> LIKE <> {id} <> {nhan['error']}"
							else:
								a=f"{h} <> {time} <> LIKE <> {id} <> {nhan['data']['msg']} <> {nhan['data']['xu']}"
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
			if h%job==0 and h >0 :
				for _ in range(10,0,-1):
					print("Đang chuyển acc khác đợi",_,end=" \r")
					sleep(1)
				break
