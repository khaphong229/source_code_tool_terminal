import os, requests as ss
from time import sleep

os.system('clear')

chon=int(input("Subpal [1] <> Ytpal [2] <> Sonuker [3] => "))

ck=input("Nhap cookie: ")

os.system('clear')

if chon==1:
	loai="subpals"
elif chon==2:
	loai="ytpals"
else:
	loai="sonuker"


head={
"Host":f"www.{loai}.com",
"user-agent":"Mozilla/5.0 (Linux; Android 10; Active 3 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36",
"cookie":ck,
}
try:
	check=ss.get(f"https://www.{loai}.com/members-area/",headers=head).text
	plan=check.split('Your Current Plan:')[1].split('</')[0]
	if "No Plan Activated" in plan:
		print("Chưa có buff")
	else:
		print("Đợi hết thời gian đi rồi quay lại")
		quit()
except:
	pass
h=0

while True:
	h+=1
	active=ss.get(f"https://www.{loai}.com/members-area/activate/",headers=head).text
	#value=active.split('var subscribers  = "')[1].split('";')[0]
	channel=active.split('var channel      = "')[1].split('";')[0]
	id=active.split('var videoId      = "')[1].split('";')[0]

	head_p={
	"Host":f"www.{loai}.com",
	"content-length":"52",
	"content-type":"application/x-www-form-urlencoded; charset=UTF-8",
	"user-agent":"Mozilla/5.0 (Linux; Android 10; Active 3 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36",
	"cookie":ck,
	}

	for i in range(20, 0, -1):
		print(f'Vui Lòng Đợi {i} _         ', end='\r')
		sleep(0.25)
		print(f'Vui Lòng Đợi {i} __        ', end='\r')
		sleep(0.25)
		print(f'Vui Lòng Đợi {i} ___       ', end='\r')
		sleep(0.25)
		print(f'Vui Lòng Đợi {i} ____      ', end='\r')

	nhan=ss.post(f"https://www.{loai}.com/members-area/sub-completed-v4.php",headers=head_p,data=f"channel={channel}&videoId={id}").json()

	if nhan['status']=="success":
		print(f"{h} | SUCCESS | {id} | {channel}")
	elif nhan['status']=="activated":
		print("Đã hết lượt rồi              ")
		break




