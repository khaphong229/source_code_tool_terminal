import os, requests as ss

ck_tds="cf_clearance=TdF2rht_c2mmeJ6IpGWSzY_JwADEvJUyi3YGFkjdsVI-1658045081-0-150; PHPSESSID=483ca6d91ee276c501fdcfaf4b35e092"


head = {
"host":"traodoisub.com",
"cookie":ck_tds,
"content-length":"591",
"content-type":"application/x-www-form-urlencoded; charset=UTF-8",
"user-agent":"Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Mobile Safari/537.36",
}

os.system("clear")

print("Facebook [1] <> Tiktok [2] <> Instagram [3] <> Youtube [4]")
chon=int(input("Please enter: "))
if chon==1:
	view="cauhinh"
	chedo="add_uid"
elif chon==2:
	view="chtiktok"
	chedo="tiktok_add"
elif chon==3:
	view="chinstagram"
	chedo="instagram_add"
elif chon==4:
	view="chyoutube"
	chedo="youtube_add"
else:
	print("nhập sai rồi")
	quit()

file=input("File containing the user id (ex: acc.txt) => ")

os.system("clear")

b=open(file,'r')
list = b.read().splitlines()

for user in list:

	print("Solving captcha!! Wait! Pls <3")

	giai=ss.get(f"http://fireender.tk/captcha_v2.php?site_key=6LeGw7IZAAAAAECJDwOUXcriH8HNN7_rkJRZYF8a&web=https://traodoisub.com/view/chtiktok/&key=atm-tool-vip").json()
	msg=giai['message']
	capp=giai['captcha']

	print(giai)





	if msg=="success":
		add=ss.post(f"https://traodoisub.com/scr/{chedo}.php",headers=head,data=f"idfb={user}&g-recaptcha-response={capp}").json()
		if "success" in add:
			print(f"{user} <> Successfully Add")
		else:
			print(f"{user} <> Error!!!")
		print(add)

	else:
		print("Captcha failed")
		continue




