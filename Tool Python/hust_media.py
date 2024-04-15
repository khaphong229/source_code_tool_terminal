import os, requests as ss
from time import sleep
from datetime import datetime
from os import path
from bs4 import BeautifulSoup

#thông tin ko thể sửa
user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'

#nhập thông tin
#apikey=int(input('Mời bạn nhập ApiKey: '))
#apikey='FaR0nbWZgHR8soJVDIVTyIui4h6W4gVoDbY0rVzRQTCWJom5AEn0at12b'
cookie='apikey=FaR0nbWZgHR8soJVDIVTyIui4h6W4gVoDbY0rVzRQTCWJom5AEn0at12b; username=kpn; dom3ic8zudi28v8lr6fgphwffqoz0j6c=17d11f54-4482-4521-ae8a-e97975ff8a9a%3A1%3A1; _gcl_au=1.1.1944348257.1700491358; _gid=GA1.2.453954789.1700491358; _ga=GA1.1.1663280729.1699408847; _ga_6CBD2E32C4=GS1.1.1700491357.1.1.1700491382.0.0.0; _ga_GN3ZRS7TQQ=GS1.1.1700491357.1.1.1700491382.0.0.0; __gads=ID=c2e53b4d5efd7ab1-22f5bc1edbe700bc:T=1699408847:RT=1700534685:S=ALNI_MY8z9Lu1nh4qY-x70tDGEYeSzxfxg; __gpi=UID=00000c81e56fe630:T=1699408847:RT=1700534685:S=ALNI_Mb23L_skMdhzyWdZojKKQU9SWjFwQ; urlsdt=/momo; money=17366; _ga_CWZJNXPN7L=GS1.1.1700534686.13.1.1700534752.0.0.0; XSRF-TOKEN=eyJpdiI6InR1dkZ6ZFhJR3J2Rngya2llL2xobkE9PSIsInZhbHVlIjoiYWtZaWlaZEVrdGJ4Sll0LzMwVm5PZS83VmVrbmJzTHlOVHFMQTVFNTNKVEZhQXgvQ0k0VnozU0lCK0tIOFBXWnd4OUZNUFdpWkRUWEVoSnpqQ3hOVmx2YjRUZHFEYVZrNnVTVWN1Qzl5MGwvRnhLUzlCY3o0K2VOaEYzMWZJOUkiLCJtYWMiOiJjYTNlZjVhNzVmYjI0NjFiNThhOTVlNGRiNTM5MWE2ZDg5NzdlYzFhODFkMDZjMjc0OTIzMzM1MjljNTlkYWVkIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6InJScmo5MlMzcVNldndKeFRodFY5d1E9PSIsInZhbHVlIjoiMFJBbEFZbWZmSi9NNnJ0N3JQT0h4c1BWcEt6ZnpwZDhEdndXOVZXM0o1RW1SQXJkSlQrZ1FUd2RLclNFRnVwMENETTY5ZitmUUQzR2JQZ0RYNDZ4N1c4TnRUa2VaY0tKWFpncVdlV2djVGdWYlZIZUVQSjZPK1I2ZS9ydkFBazQiLCJtYWMiOiI1NGUxMTc3NWU5MjI2MTkxYmM3NDM1ZTNhNjI0OWQ0YzdkNDY5ZTQ2NjYzZjNiYzVlMDk1YTczZjY0NGU4ODJiIiwidGFnIjoiIn0%3D; useragent=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExOS4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTkuMC4wLjA%3D; '

head={
"host":"hust.media",
"upgrade-insecure-requests": "1",
"cookie":cookie,
}
html=ss.get('https://hust.media/',headers=head).text
name=html.split('<h6 class="mb-0">')[1].split('</h6>')[0]
coins=html.split('#fec8c3;">')[1].split('</')[0]
print(name,coins)

apikey=html.split('?=key=')[1].split('"')[0]


# def getName(apikey):

# 	head_name={
# 	'host':'hust.media',
# 	'User-Agent':user_agent,
# 	'X-Requested-With':'XMLHttpRequest',
# 	'Content-Length':'112',
# 	'Accept':'application/json, text/plain, */*',
# 	'Content-Type':'application/json',
# 	'Origin':'https://vip.hust.media',
# 	'Referer':'https://vip.hust.media/',
# 	}

# 	data_name={
# 	"apikey":apikey,
# 	"chedo":"profile",
# 	"option":"showusername"}

# 	get=ss.post('https://hust.media/api/profile.php',data=data_name,headers=head_name).json()
# 	print(get)

def getTiktok(apikey, user_agent):

    head_tiktok = {
        'host': 'hust.media',
        'User-Agent': user_agent,
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length': '111',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'Origin': 'https://vip.hust.media',
        'Referer': 'https://vip.hust.media/',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en,vi;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    }

    data_tiktok = {
        "key": apikey,
        "chedo": "kiemtradangnhap",
        "social": "tiktok"
    }

    lay = ss.post('https://hust.media/ttc/profile.php', data=data_tiktok, headers=head_tiktok).json()
    print(lay)


getTiktok(apikey, user_agent)
