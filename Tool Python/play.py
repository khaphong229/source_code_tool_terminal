import os,requests as ss
from time import sleep
import json, sys
from datetime import datetime
from os import path
import random

def thanh():
	print("----"*20)

os.system("clear")

print("Link đăng ký tài khoản: http://playandwin.com.sg/sign-up?referral=94cd07")
print("Mã mời: 94cd07")

thanh()

ck=input("Nhập cookie: ")

head={
	'Host': 'playandwin.com.sg',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
	'X-Requested-With': 'XMLHttpRequest',
	'Cookie':ck, 
}


os.system("clear")

print("Link đăng ký tài khoản: http://playandwin.com.sg/sign-up?referral=94cd07")
print("Mã mời: 94cd07")

thanh()

user=ss.get("https://playandwin.com.sg/user-info/",headers=head).json()
print(f"{user['Name']} <> {user['Email']} <> {user['Diamond_Count']}")

thanh()

print(f"Số vé gà <> {user['Chicken_Count']}")
print(f"Số vé lợn <> {user['Pig_Count']}")
print(f"Số vé hổ <> {user['Tiger_Count']}")
print(f"Số vé gấu <> {user['Panda_Count']}")

thanh()

print(f"Số vé đang có <> {user['Ticket_Count']}")
print(f"Số năng lượng đang có <> {user['Energy_Count']}")

thanh()

gold=ss.get("https://playandwin.com.sg/gold-energy-info/",headers=head).json()
print(f"Số vé vàng đang có <> {gold['Gold_Catch_Energy_Count']}")
print(f"Số quảng cáo đang có <> {gold['Ad_Avail']}")

thanh()


h=0

while True:
	u=ss.get("https://playandwin.com.sg/user-info/",headers=head).json()
	g=ss.get("https://playandwin.com.sg/gold-energy-info/",headers=head).json()

	time = datetime.now().strftime("%H:%M")



	if u['Energy_Count']>=1:
		lay=ss.get("https://playandwin.com.sg/catch/",headers=head).json()
		h+=1

		print(f"{h} <> {time} <> {u['Chicken_Count']} gà <> {u['Pig_Count']} lợn <> {u['Tiger_Count']} hổ <> {u['Panda_Count']} gấu")

		for i in range(30, 0, -1):
			print(f'[KPNTOOL] Vui Lòng Đợi {i} _         ', end='\r')
			sleep(0.25)
			print(f'[KPNTOOL] Vui Lòng Đợi {i} __        ', end='\r')
			sleep(0.25)
			print(f'[KPNTOOL] Vui Lòng Đợi {i} ___       ', end='\r')
			sleep(0.25)
			print(f'[KPNTOOL] Vui Lòng Đợi {i} ____      ', end='\r')	

	if g['Gold_Catch_Energy_Count']>=1:
		l=ss.get("https://playandwin.com.sg/catch/?gold=1",headers=head).json()
		h+=1

		print(f"{h} <> {time} <> {u['Chicken_Count']} gà <> {u['Pig_Count']} lợn <> {u['Tiger_Count']} hổ <> {u['Panda_Count']} gấu")

		for i in range(30, 0, -1):
			print(f'[KPNTOOL] Vui Lòng Đợi {i} _         ', end='\r')
			sleep(0.25)
			print(f'[KPNTOOL] Vui Lòng Đợi {i} __        ', end='\r')
			sleep(0.25)
			print(f'[KPNTOOL] Vui Lòng Đợi {i} ___       ', end='\r')
			sleep(0.25)
			print(f'[KPNTOOL] Vui Lòng Đợi {i} ____      ', end='\r')	
	else:
		print(f"Hết lượt rồi đợi thôi",end="                           \r")









