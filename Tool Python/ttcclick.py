import os, requests as ss
from time import sleep
import os.path
from os import path
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
#cau hinh
cauhinh=ss.post(f"https://tuongtaccheo.com/cauhinh/tiktok.php",headers=head).text
#cauhinhmacdinh
chmd=cauhinh.split("Nick đang dùng: <a href='https://www.tiktok.com/@")[1].split("?'>")[0]
print("\033[37;1mCấu hình đang chạy\033[32;1m",chmd)
#cauhinhcanchay
while True:
	id=input(f"\033[37;1mNhập cấu hình cần chạy: \033[32;1m")
	if id!="":
		datch=ss.post(f"https://tuongtaccheo.com/cauhinh/datnick.php",headers=head,data={'iddat[]': id, 'loai': "tt"}).text
		if datch=="1":
			print("\033[37;1mĐặt cấu hình\033[32;1m",id,"\033[32;1mthành công")
			break
		else:
			print("\033[37;1mĐặt cấu hình\033[32;1m",id,"\033[32;1mthất bại")
	else:
		print("\033[37;1mĐang chạy cấu hình mặc định\033[32;1m",chmd)
		break
print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
chon=input(f"\033[37;1m1 => Tym | 2 => Follow | Bạn chọn: \033[32;1m")
print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
delay=int(input("\033[37;1mNhập delay: \033[32;1m"))
print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
jobtym=[]
jobfl=[]
h=0

#tym
if chon=="1":
    while True:
                get_tym=ss.get(f"https://tuongtaccheo.com/tiktok/kiemtien/getpost.php",headers=head).json()
                if len(get_tym)!=0:
                    for x in get_tym:
                        id = x['idpost']
                        link = x['link']
                        h+=1
                        print(f"\033[37;1m[\033[32;1m{h}\033[37;1m][\033[32;1mTYM\033[37;1m][\033[32;1m{id}\033[37;1m]")
                        jobtym.append(id)
                        os.system(f'xdg-open {link}')
                        for i in range(delay, 0, -1):
                            print(f'\033[1;95m[KPNTOOL] Vui Lòng Đợi {i} _         ', end='\r')
                            sleep(0.25)
                            print(f'\033[1;94m[KPNTOOL] Vui Lòng Đợi {i} __        ', end='\r')
                            sleep(0.25)
                            print(f'\033[1;93m[KPNTOOL] Vui Lòng Đợi {i} ___       ', end='\r')
                            sleep(0.25)
                            print(f'\033[1;92m[KPNTOOL] Vui Lòng Đợi {i} ____      ', end='\r')
                            sleep(0.25)
                        if len(jobtym)==10:
                            print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
                            id=','.join(jobtym)
                            nhan=ss.post('https://tuongtaccheo.com/tiktok/kiemtien/nhantien.php', headers=head, data={"id": id}).json()
                            print("\033[37;1m=>",nhan)
                            jobtym.clear()
                            print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
                else:
                    print("\033[37;1mHết nhiệm vụ", end='\r')
if chon=="2":
        while True:
                get_fl=ss.get(f"https://tuongtaccheo.com/tiktok/kiemtien/subcheo/getpost.php",headers=head).json()
                if len(get_fl)!=0:
                    for x in get_fl:
                        id = x['idpost']
                        user = x['link']
                        h+=1
                        link=f"https://www.tiktok.com/@{user}"
                        print(f"\033[37;1m[\033[32;1m{h}\033[37;1m][\033[32;1mFOLLOW\033[37;1m][\033[32;1m{user}\033[37;1m]")
                        jobfl.append(id)
                        os.system(f'xdg-open {link}')
                        for i in range(delay, 0, -1):
                            print(f'\033[1;95m[KPNTOOL] Vui Lòng Đợi {i} _         ', end='\r')
                            sleep(0.25)
                            print(f'\033[1;94m[KPNTOOL] Vui Lòng Đợi {i} __        ', end='\r')
                            sleep(0.25)
                            print(f'\033[1;93m[KPNTOOL] Vui Lòng Đợi {i} ___       ', end='\r')
                            sleep(0.25)
                            print(f'\033[1;92m[KPNTOOL] Vui Lòng Đợi {i} ____      ', end='\r')
                            sleep(0.25)
                        if len(jobfl)==10:
                            print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
                            id=','.join(jobfl)
                            nhan=ss.post('https://tuongtaccheo.com/tiktok/kiemtien/subcheo/nhantien.php', headers=head, data={"id": id}).json()
                            print("\033[37;1m=>",nhan)
                            jobfl.clear()
                            print("\033[33;1m▪\033[32;1m▪\033[31;1m▪\033[36;1m▪"*15)
                else:
                    print("\033[37;1mHết nhiệm vụ", end='\r')










1