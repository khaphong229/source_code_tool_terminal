import os, requests as ss
from time import sleep

os.system('clear')

#chon=int(input("Subpal [1] <> Ytpal [2] <> Sonuker [3] => "))



#cka=input("Nhap cookie subpal: ")

#ckb=input("Nhap cookie ytpal: ")

#ckc=input("Nhap cookie sonuker: ")

cka="_ga=GA1.1.1361896543.1692621197; _pbjs_userid_consent_data=3524755945110770; _pubcid=7c406963-ff05-4e4d-8cfb-ce77d44555fa; _lr_env_src_ats=false; Neustar-Fabrick ID=%7B%22fabrickId%22%3A%22E1%3AAEu4xAgve0OkcEfV-X0UmhsHo4cTF23jxI6ARwN3cJ87boIG_aBYFlORd7a29OsNPhzOL53ROazZ850zaBo5BvAK4l_4khy1iVPgpl1SQFT4GspA_O_NYDI3_gGDbJGZ%22%7D; __gads=ID=2aaa64bc2b62abd7:T=1692625583:RT=1692625583:S=ALNI_MYOYakKYBDMf0U7tyYsU1LtJrhjhg; __gpi=UID=00000c3057864c87:T=1692625583:RT=1692625583:S=ALNI_MYPmRSuNzKTO2yeDWCNFz4RpwOY4Q; cto_bidid=PhTSpF9SYU5JNzIlMkYlMkJYVlNLbmh4Qmt0bEZGVE00a2dwd0J6U2dLWW1hYW56YWg3dkUlMkIyTmdaVjJTM2pHQzB1dGYzNTlyRzhMRkR4QXY4R0EwZ0NvZzltVjZCeFZieFVjMFhOeVJWOUtmZm44RE1CNCUzRA; cto_dna_bundle=x6NDDF8wbm1EZEVHJTJGSVFvVGlNQjJIeU9lU0cxeWNLS2RUNHZTZkJrS3lCblVmQkJLQmY0czUlMkJvMG1LblBJbjR2Y1pzMU9RUE10MVVIREZybVFXV3REQ21Fb3clM0QlM0Q; PHPSESSID=qtoo3olhj1qg35rotgseoqm40i; __cf_bm=lw0csOSxZdFX2ECXNFoIGA0v6x3z3TzUSFBqMP7KPeo-1692671649-0-AYmZManwm7+fAfCZJWgHiO2h8F4iSgGokvGo5IIwJ+ScLSKDNwKgfQMGyNSGSPhRVH0iwtughzbg3CChr4pDQIE=; _ga_6WTH13ELBM=GS1.1.1692671651.3.1.1692671676.0.0.0; cto_bundle=giZKSl8wbm1EZEVHJTJGSVFvVGlNQjJIeU9lU0xmOWhpclVYUlBTNE8zTUV4SkRocFAydmxhaWV5cHNPSDd6MyUyRnVTdEg3a05WbWV5aCUyQlJQZW41QUVuUWlqMllWQnlxZUpuZm5WWEpjNkduSEFsUWVsRnJJRldxSjBjczExd1ZCNSUyQjdUMVBtT3hBY1VEZG1OMGNSOG1GV1Z3dDVjUSUzRCUzRA; useragent=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNS4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTUuMC4xOTAxLjIwMw%3D%3D; "



ckb="_ga=GA1.1.1955567299.1692621323; hblid=J3feeXgn14LLHoaD276LI0IkaCFbjrB3; olfsk=olfsk9989476632891796; paddos_HJxyy=1; PHPSESSID=6eso1inm2mpfl59j1tlrsp0ggq; __cf_bm=eqEI5txK2yK5Ycx0Xl.wBg8bXgM7RyTB_RXokT1whZw-1692671687-0-AbQyCsViC/j7NYoqmGp8BP/morNszNvY1ma8AoLjm/CbHZdLvvK0pQHKus6J8RF27LkYjBW4lOMd8ttPx4KEu3o=; wcsid=mWjZeYHGVMdUbJG5276LI0I3FBoSAzka; _okdetect=%7B%22token%22%3A%2216926716907400%22%2C%22proto%22%3A%22about%3A%22%2C%22host%22%3A%22%22%7D; _okbk=cd4%3Dtrue%2Cvi5%3D0%2Cvi4%3D1692671691077%2Cvi3%3Dactive%2Cvi2%3Dfalse%2Cvi1%3Dfalse%2Ccd8%3Dchat%2Ccd6%3D0%2Ccd5%3Daway%2Ccd3%3Dfalse%2Ccd2%3D0%2Ccd1%3D0%2C; _ok=1441-802-10-6072; _ga_VWXD5PXED8=GS1.1.1692671690.3.1.1692671702.0.0.0; _oklv=1692671763951%2CmWjZeYHGVMdUbJG5276LI0I3FBoSAzka; useragent=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNS4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTUuMC4xOTAxLjIwMw%3D%3D;"


ckc="_ga=GA1.1.1688622782.1692620808; PHPSESSID=eum11h0kdnjusb2kep97jc2o37; __cf_bm=wGIHfmfSlk_Q4BHrk9X_3uAahKecvi8cCjRXP5lLJOU-1692671712-0-ASrwIelwhmW8KXgpq+WZAG+Vc62bt+5TX7dX8LrqX5dn2AUnqlqnV91acrUpPu8wPxPBAMAdyH0wS9HLBqRwg+4=; _ga_PYT4DLL427=GS1.1.1692671713.3.1.1692671761.0.0.0; useragent=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNS4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTUuMC4xOTAxLjIwMw%3D%3D; "


os.system('clear')

#if chon==1:
	#loai="subpals"
#elif chon==2:
#	loai="ytpals"
#else:
	#loai="sonuker"



def chay(loai,ck):
	head={
	"Host":f"www.{loai}.com",
	"user-agent":"Mozilla/5.0 (Linux; Android 9; SM-S906N Build/PQ3B.190801.08041932) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36",
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
		try:
			channel=active.split('var channel      = "')[1].split('";')[0]
			id=active.split('var videoId      = "')[1].split('";')[0]
		except:
			break

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

while True:


	chay("subpals",cka)

	chay("ytpals",ckb)

	chay("sonuker",ckc)

	for _ in range(43300,0,-1):
		print("                        ",end=" \r")
		sleep(0.25)
		print("Chờ",end=" \r")
		sleep(0.25)
		print("Chờ",_,end=" \r")
		sleep(0.25)
		print("Chờ",_,"giây",end=" \r")
		sleep(0.25)