import os, requests as ss
from time import sleep
from datetime import datetime
from os import path

os.system("clear")

tk= '83acd530801611ebbbb847d8e616720c'
devicetk= 'c9twQ4VKRU-TfAdKWpLCq9:APA91bH-1tL6xwYQ3kSDS0WI8Vvz1H4pkWn3qVk0kNr1YeJgppldY_DkwJ8ln2WT9kBudyUqO2um73akd1ENdYQGhxd6wtiRzb7bdaXZPIjeFAodiju66czCZR9LI4a4O7-Zkq_fGBQc'
device= 'OPPO A37f'
versioncode = '178'

head={
"Host":"tuberocket.app:3000",
"token":tk,
"versionCode":versioncode,
"device":device,
"deviceToken":devicetk,
}


sign=ss.post("http://tuberocket.app:3000/api/signIn",headers=head).json()
token=sign['result']['token']


head_a={
"Host":"tuberocket.app:3000",
"token":token,
}


head_b={
"Host":"tuberocket.app:3000",
"token":token,
"Content-Length":"71",
"Content-Type":"application/json; charset=UTF-8",
}

mem=ss.get("http://tuberocket.app:3000/api/member",headers=head_a).json()
mail=mem['result']['email']
coin=mem['result']['coin']

print(f"Email: {mail} • coin {coin}")
while True:
	tc_b = ss.get("http://tuberocket.app:3000/api/video",headers=head_a).json()
	id = tc_b['result']['videoId']
	time = tc_b['result']['playSecond']

	for i in range(time, 0, -1):
		print(f'\033[1;95m[KPNTOOL] Vui Lòng Đợi {i} _         ', end='\r')
		sleep(0.25)
		print(f'\033[1;94m[KPNTOOL] Vui Lòng Đợi {i} __        ', end='\r')
		sleep(0.25)
		print(f'\033[1;93m[KPNTOOL] Vui Lòng Đợi {i} ___       ', end='\r')
		sleep(0.25)
		print(f'\033[1;92m[KPNTOOL] Vui Lòng Đợi {i} ____      ', end='\r')


	nhan = ss.put("http://tuberocket.app:3000/api/video",headers=head_b,data='{"id":"'+id+'","playCount":0,"playSecond":0,"boost":0,"status":""}').json()
	xu1 = nhan['result']['coin']
	print(f"Nhận thành công >> {xu1}                         ")

