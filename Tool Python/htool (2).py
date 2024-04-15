#Vip
import os,json,re,sys
import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
try:
	import requests
except:
	os.system('pip install --upgrade pip && pip install requests')
	import requests
os.system("clear")
# Tool 
def logo():
    log="""
\033[1;36m
		 /$$   /$$ /$$$$$$$  /$$   /$$
		| $$  /$$/| $$__  $$| $$$ | $$
		| $$ /$$/ | $$  \ $$| $$$$| $$
		| $$$$$/  | $$$$$$$/| $$ $$ $$
		| $$  $$  | $$____/ | $$  $$$$
		| $$\  $$ | $$      | $$\  $$$
		| $$ \  $$| $$      | $$ \  $$
		|__/  \__/|__/      |__/  \__/
"""
    for h in log:
       sys.stdout.write(h)
       sys.stdout.flush()
       sleep(0)
       
def clr():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system('clear') 

clr()
def clear():
    if(sys.platform.startswith('win')):
        os.system('cls')
    else:
        os.system('clear')
gome_token = []
def get_token(input_file):
    for cookie in input_file:
        header_ = {
            'authority': 'business.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cache-control': 'max-age=0',
            'cookie': cookie,
            'referer': 'https://www.facebook.com/',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',

        }
        try:
            home_business = requests.get('https://business.facebook.com/content_management', headers=header_).text
            token = home_business.split('EAAG')[1].split('","')[0]
            cookie_token = f'{cookie}|EAAG{token}'
            gome_token.append(cookie_token)
        except:
            pass
    return gome_token

def share(tach, id_share):
    cookie = tach.split('|')[0]
    token = tach.split('|')[1]
    he = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate',
        'connection': 'keep-alive',
        'content-length': '0',
        'cookie': cookie,
        'host': 'graph.facebook.com'
    }
    try:
        res = requests.post(f'https://graph.facebook.com/me/feed?link=https://m.facebook.com/{id_share}&published=0&access_token={token}', headers=he).json()
    except:
        pass
    
    
def main_share():
    clear()
    logo()
    input_file = open(input("\033[1m\033[38;5;51mNhập File Chứa Cookie Fb: \033[1;35m")).read().split('\n')
    id_share = input("\033[1m\033[38;5;51mNhập ID Bài Viết: \033[1;35m")
    total_share = int(input("\033[1m\033[38;5;51mNhập Số Lượt Share: \033[1;35m"))
    delay = int(input("\033[1m\033[38;5;51mNhập Delay: \033[1;35m"))
    all = get_token(input_file)
    total_live = len(all)
    if total_live == 0:
        sys.exit()                                      
    print('\033[1;37m---------------------------------------')
    stt = 0
    while True:
        for tach in all:
            stt = stt + 1
            threa = threading.Thread(target=share, args=(tach, id_share))
            threa.start()
            threa.join()
            print(f"\033[1;97m[{stt}] SUCCESS | ID: \033[1m\033[38;5;51m{id_share}")
        time.sleep(delay)
        if stt > total_share:
            break
    gome_token.clear()
    input('\n\033[38;5;245m[\033[38;5;9m+\033[38;5;245m] \033[38;5;9mBấm Enter Để Tiếp Tục\033[0m')
while True:
    try:
        main_share()
    except KeyboardInterrupt:
        print('\n\033[38;5;245m[\033[38;5;9m!\033[38;5;245m] \033[38;5;9m.\033[0m')
        sys.exit()