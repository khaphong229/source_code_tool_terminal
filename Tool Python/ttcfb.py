import os,requests as ss
from time import sleep
import json, sys
from datetime import datetime
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
head_ttc = {
"cookie":ck_ttc,
"Host":"tuongtaccheo.com",
"x-requested-with":"XMLHttpRequest",
"user-agent":ua,
}

head_ch = {
"cookie":ck_ttc,
"Host":"tuongtaccheo.com",
"x-requested-with":"XMLHttpRequest",
"user-agent":ua,
"content-length": "35",
"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
}

#lấy thông tin
print("\033[37;1mTOOL LIKE FACEBOOK BY KPN".center(60))
print("-"*65)
tkk=ss.post(f"https://tuongtaccheo.com/logintoken.php",headers=head_ttc,data={"access_token":api}).text
print("=>",tkk)
print("-"*65)

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

job=int(input("Bạn muốn làm bao nhiêu job thì đổi acc: "))
delay=int(input("Nhập delay: "))

def ch(ck,head_ch):
    print("-"*65)
    head = {
    "cookie":ck,
    }
    lay=ss.get("https://mbasic.facebook.com/home.php?ref_component=mbasic_home_header&ref_page=%2Fwap%2Fprofile_timeline.php&refid=17",headers=head).text
    idacc=lay.split('?av=')[1].split('&amp;')[0]

    get_name=ss.get(f'https://mbasic.facebook.com/profile.php?id={idacc}&_rdr',headers=head).text
    name=get_name.split('<head><title>')[1].split('</')[0]

    datch=ss.post(f'https://tuongtaccheo.com/cauhinh/datnick.php',headers=head_ch,data=f"iddat[]={idacc}&loai=fb").text

    if datch=="1":
        print(f"{name} <> {idacc} <> Đặt cấu hình thành công")
    else:
        print(f"{name} <> {idacc} <> Đặt cấu hình thất bại")
        return False

    print("-"*65)

def likepost(ck,id_job):
    head = {"cookie":ck}
    link = ss.get("https://mbasic.facebook.com/"+id_job,headers=head).url
    b = ss.get(link,headers=head).text
    try:
        url = "https://mbasic.facebook.com/a/like.php?"+b.split('/a/like.php?')[1].split('"')[0].replace('amp;','')
        like = ss.get(url,headers=head,allow_redirects=False).text
        if like=="":
            return True
        elif "Tài khoản của bạn hiện bị hạn chế" in like:
            return False
        else:
            return like
    except:
        return "loi"



h=0

with open('fb_kpn.txt') as f:
    size=len([0 for _ in f])
    soacc=int(size)

head_nhan = {
"cookie":ck_ttc,
"Host":"tuongtaccheo.com",
"x-requested-with":"XMLHttpRequest",
"user-agent":ua,
"content-length": "19",
"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
}

while True:
    for i in range(1,int(soacc)+1):
        c=i-1
        b=open('fb_kpn.txt','r')
        list = b.read().splitlines()
        ck=list[c]

        cauhinh=ch(ck,head_ch)
        if cauhinh== False:
            continue

        sleep(2)

        while True:
            get_job=ss.get(f'https://tuongtaccheo.com/kiemtien/getpost.php',headers=head_ttc).json()
            if get_job==[]:
                print("Hết job ...",end="                                 \r")

            else:
                for x in get_job:
                    print(f"Đang có {len(get_job)} nhiệm vụ",end="                             \r")
                    #try:
                    id_job=x['idpost']

                    print(f"Đang like bài {id_job}",end="                             \r")

                    check=likepost(ck,id_job)

                    time = datetime.now().strftime("%H:%M")

                    if check==False:
                        print("Tài khoản của bạn hiện bị hạn chế")
                    elif check=="loi":
                        h+=1
                        #print(f"{h} <> {time} <> LIKE <> {id_job} <> Link lỗi rồi")
                        pass
                    else:
                        
                        h+=1
                        nhan=ss.post(f'https://tuongtaccheo.com/kiemtien/nhantien.php',headers=head_nhan,data=f"id={id_job}").json()

                        if "error" in nhan:
                            a=f"{h} <> {time} <> LIKE <> {id_job} <> {nhan['error'].split(',')[0]}"
                        else:
                            a=f"{h} <> {time} <> LIKE <> {id_job} <> {nhan['mess'].split(',')[1]}"
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
                    #except:
                        #pass
            if h%job==0 and h>0:
                for _ in range(10,0,-1):
                    print("Đang chuyển acc khác đợi",_,end=" \r")
                    sleep(1)
                break
