import os, requests as ss
from time import sleep


os.system('clear')

chon=int(input("""1 | Like Youtube
2 | Pinterest Follow
=> """))

os.system('clear')


ck=input("Nhập cookie like4like: ")
if chon==1:
	aut=input("Nhập authorization ytb: ")
	cookie=input("Nhập cookie ytb: ")
elif chon==2:
	pin_ex=input("Nhập x-pinterest-experimenthash: ")
	ck_pin=input("Nhập cookie pinterest: ")

os.system('clear')

def thanh():
	print("---"*10)


if chon==1:
	def like(link, cookie, aut):
		head={
		'Host':'api.kpb-fia.com',
		'User-Agent':'Mozilla/5.0 (Linux; Android 9; RMX1811) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
		'Accept':'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
		}

		data_sub={
		"KPB":"YOUTUBE",
		"TYPE":"LIKE",
		"LINK-VIDEO":link,
		"COOKIE":cookie,
		"AUTHORIZATION":aut,
		}

		sub=ss.post("https://api.kpb-fia.com/api/kpb-coder.php",data=data_sub,headers=head).json()
		#print(sub)
		if sub['kpb-check']=="1":
			return True
		else:
			return False


head={
	"host":"www.like4like.org",
	"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
	"cookie":ck,
}

head_post={
	"host":"www.like4like.org",
	"content-length":"163",
	"content-type":"application/x-www-form-urlencoded; charset=UTF-8",
	"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
	"cookie":ck,
}

head_pin={
	"host":"www.like4like.org",
	"content-length":"166",
	"content-type":"application/x-www-form-urlencoded; charset=UTF-8",
	"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
	"cookie":ck,
}


if chon==2:
	def fl_pin(id):
		head={
		'Host':'www.pinterest.com',
		'x-requested-with':'XMLHttpRequest',
		'accept':'application/json, text/javascript, */*, q=0.01',
		'user-agent':'Mozilla/5.0 (Linux; Android 10; Active 3 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36',
		'cookie':ck_pin,
		'x-pinterest-experimenthash':pin_ex,
		}


		head_fl={
		'Host':'www.pinterest.com',
		'content-length':'127',
		'x-requested-with':'XMLHttpRequest',
		'x-csrftoken':ck_pin.split('csrftoken=')[1].split(';')[0],
		'content-type':'application/x-www-form-urlencoded',
		'accept':'application/json, text/javascript, */*, q=0.01',
		'user-agent':'Mozilla/5.0 (Linux; Android 10; Active 3 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36',
		'cookie':ck_pin,
		'x-pinterest-experimenthash':pin_ex,
		}


		pin=ss.get(f"https://www.pinterest.com/resource/UserResource/get/?source_url=%2F{id}%2F&data=%7B%22options%22%3A%7B%22username%22%3A%22{id}%22%2C%22field_set_key%22%3A%22quicksave%22%7D%2C%22context%22%3A%7B%7D%7D&_=1675005356344", headers=head).json()
		user=pin['resource_response']['data']['id']
		#print(user)


		fl=ss.post("https://www.pinterest.com/resource/UserFollowResource/create/",headers=head_fl,data=f"source_url=%2F{id}%2F&data=%7B%22options%22%3A%7B%22user_id%22%3A%22{user}%22%7D%2C%22context%22%3A%7B%7D%7D").json()
		#print(fl['resource_response']['status'])

user=ss.get("https://www.like4like.org/api/get-user-info.php",headers=head).json()
print(f"you have {user['data']['credits']} credits")

thanh()
h=0
if chon==1:
	while True:
		task=ss.get("https://www.like4like.org/api/get-tasks.php?feature=youtube",headers=head).json()
		try:
			link=task['data']['tasks'][0]['url']
			id=task['data']['tasks'][0]['idlink']
			taskid=task['data']['tasks'][0]['taskId']
			cod=task['data']['tasks'][0]['code3']
			h+=1
			#print(f"{id} | {taskid}")

			start=ss.get(f"https://www.like4like.org/api/start-task.php?idzad={id}&vrsta=like&idcod={taskid}&feature=youtube&_=1672559854723",headers=head).json()
			code=start['data']['codedTask']


			like(link,cookie,aut)

			check=ss.post("https://www.like4like.org/checkurl.php",headers=head,data=f"https://www.youtube.com/watch?v={id}").text
			#print(check)

			nhan=ss.post("https://www.like4like.org/api/validate-task.php",headers=head_post,data=f"url=https://www.youtube.com/watch?v={id}&idzad={taskid}&idlinka={id}&idclana={cod}&cnt=true&vrsta=like&feature=youtube&addon=false&version=").json()
			print(f"{h} | {id} | {taskid} | {nhan['data']['credits']} credits")

			for _ in range(11,0,-1):
				print("                        ",end=" \r")
				sleep(0.25)
				print("Chờ",end=" \r")
				sleep(0.25)
				print("Chờ",_,end=" \r")
				sleep(0.25)
				print("Chờ",_,"giây",end=" \r")
				sleep(0.25)
		except:
			print("Hết job ...",end=" \r")
			continue

elif chon==2:

	while True:
		task=ss.get("https://www.like4like.org/api/get-tasks.php?feature=pinterestfol",headers=head).json()
		try:
			link=task['data']['tasks'][0]['url']
			id=task['data']['tasks'][0]['idlink']
			taskid=task['data']['tasks'][0]['taskId']
			cod=task['data']['tasks'][0]['code3']
			h+=1
			#print(f"{id} | {taskid}")

			start=ss.get(f"https://www.like4like.org/api/start-task.php?idzad={id}&vrsta=follow&idcod={taskid}&feature=pinterestfol&_=1672559854723",headers=head).json()
			code=start['data']['codedTask']

			fl_pin(id)

			check=ss.post("https://www.like4like.org/checkurl.php",headers=head,data=f"url={link}").text
			#print(check)

			nhan=ss.post("https://www.like4like.org/api/validate-task.php",headers=head_pin,data=f"url={link}&idzad={taskid}&idlinka={id}&idclana={cod}&cnt=true&vrsta=follow&feature=pinterestfol&addon=false&version=").json()
			print(f"{h} | {id} | {taskid} | {nhan['data']['credits']} credits")

			for _ in range(11,0,-1):
				print("                        ",end=" \r")
				sleep(0.25)
				print("Chờ",end=" \r")
				sleep(0.25)
				print("Chờ",_,end=" \r")
				sleep(0.25)
				print("Chờ",_,"giây",end=" \r")
				sleep(0.25)
		except:
			print("Hết job ...",end=" \r")
			continue





