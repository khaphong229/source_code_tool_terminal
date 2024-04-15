import os, requests as ss
from time import sleep


ck="_gid=GA1.2.451289664.1674996299; _gat_gtag_UA_21175192_9=1; PHPSESSID=s0slp8n9cfq32pqt0kn7fss4o0; _ga_DVWFX221E1=GS1.1.1675161610.7.1.1675161757.0.0.0; _ga=GA1.1.321142740.1672559229; useragent=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgNi4xOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTA5LjAuMC4wIFNhZmFyaS81MzcuMzY%3D; _uafec=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F109.0.0.0%20Safari%2F537.36; "

aut="SAPISIDHASH 1670843432_12ef27fa3e04cedb085b0f12d4edd50bc9d0b1b2"
cookie="VISITOR_INFO1_LIVE=lxdBFQ3hQlQ;PREF=f4=4000000&tz=Asia.Saigon&f5=20000&f7=100&f6=40000000;YSC=My-wj9fuWZM;GPS=1;SID=RggSmg17UQVxpQtA1rUNNRaivtPfu8YWPIxRZajbeeHqx27QfAAQZ9JYRO9rKuyA4upBVA.;__Secure-1PSID=RggSmg17UQVxpQtA1rUNNRaivtPfu8YWPIxRZajbeeHqx27QCmtKxmLXaVfNoe736fmzHw.;__Secure-3PSID=RggSmg17UQVxpQtA1rUNNRaivtPfu8YWPIxRZajbeeHqx27QvzU_mmNoDLrZQdEs6j4eXQ.;HSID=AkqaScQYs_k_uxqnt;SSID=AwlzcIyT3BMkhizuW;APISID=LzftCrFNvHlS-VqH/AWrxS4nJUmJ2X0A-5;SAPISID=eOM5aKgaN71xoXIP/A53UjdEA1KPa61y2d;__Secure-1PAPISID=eOM5aKgaN71xoXIP/A53UjdEA1KPa61y2d;__Secure-3PAPISID=eOM5aKgaN71xoXIP/A53UjdEA1KPa61y2d;LOGIN_INFO=AFmmF2swRgIhALBrm0hmJsOD-8kJqfHH2RIvL_-xMXMTRRNZpgqtKu3qAiEAsI1xTdzrgkum4Cp9-SdtpzcxsGRZm1IE7pZMG5QJg0g:QUQ3MjNmeFhlNlZBUnFOS1I1SDk1QUlSaktDY2tfZm5LbldyQ01Na1FhSWtILUxFZmJ0aVplWF9reXpWVHIxMnFGOGt4Rl9VWjFqVlFFRlZTTzVaNjJWRk1lQ0RUeGJDLXF1UG5PdjMzWEl6dDBfNWZVZjNNUFdENGp5dzJxOEd4VGdVZXFNMGNtbGJFQ19hT3Q2SV9HZWVCMlJaOVRfQjln;SIDCC=AIKkIs0ZOoTSUNV4l_ydeghhZeQGl1UBWUzOy0wnkBcb99FXOfhlmgMbY6CTP3LEoEkweLs26g;__Secure-1PSIDCC=AIKkIs38_6qyMUEJ3QrweZVPI-_QN_FMNaplYfVQ8GiEsXFjVJT9LubBgm7tCfcJh6Sg7Ci23w;__Secure-3PSIDCC=AIKkIs2OtiPqU2NSpiPHZqKiHv_BMqRUYUjdpRsC1BdxaTYiXpsTEhsTbts2GoqjmRK0DkgtPT8"


os.system('clear')

chon=int(input("""1 | Like Youtube
2 | Pinterest Follow
=> """))

os.system('clear')


#ck=input("Nhập cookie like4like: ")
#if chon==1:
	#aut=input("Nhập authorization ytb: ")
	#cookie=input("Nhập cookie ytb: ")
#elif chon==2:
	#pin_ex=input("Nhập x-pinterest-experimenthash: ")
	#ck_pin=input("Nhập cookie ytb: ")

#os.system('clear')

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



ck_pin='_auth=1; _b="AWXqyST/CHBG8pMY34t73hXVKR0Nc28hXoSSHbv44nrVbA2e7OpPpSiZUn28MoMWBrY="; _pinterest_sess=TWc9PSZPZ0RkbHJYUDhncjN4dTVqQ2ltV29DZjlYS2tqM0xLQ2tLbmdXMkFORE9KSXhwa0hRcU5TVU95cTU1djQvbFQrdlpiV2wxZjd5dEwvU1NTRnBmak1ZelhpQklRQXZBQ2FkLzRZNXJpWm1pMkQvNjlSdGMvRjNsUUsvK0tidUdiTWZnYUxtblc2Y0ZnaWZLVWJPcSthcEk4QU1kbEJ5UWI0c0JjMFBIcUtycWNJVk5pSTJPNUZYa2VNZWovbHl1Ukk3OVExMFB6M05JZjhZQkV1dnNSMFB2cXhTU1cydko1eS9Qb2dhUEs5TlZTTjdoUG56Z1kyWXozMkduVHFERnJiUmlnMWVnOXhEZEJFTVQxNFF1aXkrYzMyOFcwa05laURDU0xteVZvN1NpNUFKcXFER201NWFLUTEwTHl4NzdxWXNaOE9uakJmNUZHZTJVZ3VVRkZSbmFuNkFReWJzZUFmMzNTNnpaTXNKeW5kNG5wUFk2M25qc3JoMlZBemYvS1Q2ZTBSbUovdGhMOElxTlNGL3ZkT1J1dnNJWG14MCtXd1ltNmEybmF0bHQ5bUxFd2paUWRqcHRWN00zM3UxRUZTJkJCWENiQjhPTUs2Y1llZDNQS2l4dkhOaWpCMD0=; csrftoken=005873c318f9a94ca0f2046b4d9ed238; _pinterest_cm="TWc9PSZuRjBqTmZTclVqUkdMQ1ZHaTJuSkNlNXNFaVdCeU1jMW9TUVpGei9KRjFuMHE3V2lhRFFTV1g1NkthdjkyZmpuaHBmMDFaOW5zbXl3S1Z1Q0lWb0Fra1dHZGhZejBPNG16dm5HMG9ETjBjSE8rV1EwbGp3Q3FTT0M3OEZ1eDhCSjBGaldLR0t5Q3ZjSW1leGJpUzR3Wk1WR1RDZzJ6QnZFdkZMczhuNGlQN1pmQUllbEhnZ3E2TVJRYWFKK1ZKQVomNjEvMmV0cjlrVnF0NmdxYndoMlBqd3JVOVNRPQ=="; _routing_id="c6b21057-af5e-4ea5-9c51-653727db7f4e"; sessionFunnelEventLogged=1; ajs_anonymous_id=0695cc55-68dd-4949-aa0e-0cdad2126229; cm_sub=none'

pin_ex="43c47d38087f8557c38d7b004dc33808d29e618e2c7790209f2724f98b817f99e905cb8cd20571f5e6d15ef54cbadabd65416195bd8416d77801ed8fb7881899"

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





