import random
import time
import requests, os
from os.path import exists
from datetime import datetime
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
global followsolan
global likesolan
class VipIg():
    def __init__(self, cookie, cookieIg,delaylike, delayfollow):
        super().__init__()
        self.cookieIg = cookieIg
        self.cookie = cookie
        self.delaylike = delaylike
        self.delayfollow = delayfollow
        #self.nv = nv
    def likeIG(self, link):
        try:
            post = requests.get(link + "/", headers=self.head,).text
            id=post.split('{"media_id":"')[1].split('"')[0]
            like = requests.post("https://www.instagram.com/web/likes/"+id+"/like/", data="", headers=self.headers).text
            if '{"status":"ok"}' in like:
                return True
            elif '"spam":true' in like:
                return False
            else:
                return "notblock"
        except:
            return "wait"
    def followIG(self, id):
        try:
            follow = requests.post("https://www.instagram.com/web/friendships/"+id+"/follow/", data="", headers=self.headers).text
            #print(follow)
            if '{"result":"following","status":"ok"}' in follow or '{"result":"requested","status":"ok"}' in follow:
                return True
            elif '"spam":true' in follow:
                return False
            elif  "Please wait a few minutes before you try again." in follow:
                return "wait"
        except:
            return "wait"
    def dat_nick(self, id):
        try:
            username = requests.get(f"https://i.instagram.com/api/v1/users/{id}/info/", headers=self.headers).json()
            if 'checkpoint_url' in username:
                return "dcm"
            username=username["user"]["username"]
            cauhinh = requests.get("https://vipig.net/cauhinh/index.php", cookies=self.cookie, headers=self.headvipig).text
            if id not in cauhinh:
                nhapnick = requests.post("https://vipig.net/cauhinh/nhapnick.php", data="link="+username, cookies=self.cookie, headers=self.headvipig).text
                if nhapnick == "":
                    print("Thêm Acc:", username, "thành công")
            datnick = requests.post("https://vipig.net/cauhinh/datnick.php", data="iddat[]="+id, cookies=self.cookie, headers=self.headvipig).text
            if datnick == "1":
                print("<> Đặt nick: "+username+" thành công")
        except:
            pass
    def getMission(self, type):
        if type == "like":
            #try:
                url = "https://vipig.net/kiemtien/getpost.php"
                misson = requests.get(url, cookies=self.cookie, headers=self.headvipig).json()
                if len(misson) < 1:
                    print("[~] Hết job like", end=" \r")
                    return "hetjob"
                id=misson[0]["idpost"]
                link = misson[0]["link"]
                check = self.likeIG(link)
                if check == True:
                    ok = 0
                    
                elif check == False:
                    print(FAIL+'Block like')
                    return "block"
                elif check == "wait":
                    print('"Vui lòng đợi một vài phút trước khi bạn thử lại. Đợi 5s"')
                    return "wait"
                elif check == "notblock":
                    print('Chịu bỏ qua, like này bị gì',end=" \r")
                    return "notblock"
                success = requests.post("https://vipig.net/kiemtien/nhantien.php", data="id="+id, cookies=self.cookie, headers=self.headvipig)
                #print(success.text)
                if "Thành công" in success.text:
                    date = datetime.now().strftime("%H:%M")
                    print(date+" <> Like Success: <> ", id)
                    home = requests.get("https://vipig.net/home.php", cookies=self.cookie, headers=self.headvipig).text
                    soduchinh = home.split('id="soduchinh">')[1].split('<')[0]
                    useracc = home.split('Chào mừng <i>')[1].split('<')[0]
                    print(success.json()["mess"]+","+" <> Xu:",soduchinh," <> "+"Tài khoản: "+useracc)
                for l in range(self.delaylike, -1, -1):
                    time.sleep(1)
                    print("Vui lòng đợi "+str(l)+" giây",end=" \r")
            #except:
                #
                #print(""+OKGREEN+"[~] Hết job like", end=" \r")
                #return "hetjob"
        elif type == "follow":
            listid = ""
            index = 0
            #checknv = 5
            while True:
                #try:
                    url = "https://vipig.net/kiemtien/subcheo/getpost.php"
                    misson = requests.get(url, cookies=self.cookie, headers=self.headvipig).json()
                    if len(misson) < 5 and len(listid) == 0:
                        print("Không đủ nv trên web bỏ qua")
                        return "no misson"
                    id = misson[0]["soID"]
                    if id in listid:
                        continue
                    check = self.followIG(id)
                    if check == True:
                        date = datetime.now().strftime("%H:%M")
                        print(date+" <> Follow Success: <> ", id)
                    elif check == False:
                        print('Block follow')
                        return "block"
                    elif check == "wait":
                        print("Vui lòng đợi một vài phút trước khi bạn thử lại")
                        return "wait"
                    listid = listid + id + ","
                    if index == 4:
                        listid = listid + id
                        break
                    index += 1
                    for f in range(self.delayfollow, -1, -1):
                        time.sleep(1)
                        print(+"Vui lòng đợi "+str(f)+" giây",end=" \r")
                #except:
                    #print("[~] Hết job follow", end=" \r")
            #if len(listid.split(",")) > 4:
                #print("Đủ 5 nv nhận tiền")
            success = requests.post("https://vipig.net/kiemtien/subcheo/nhantien2.php", data="id="+listid, cookies=self.cookie, headers=self.headvipig)
            #print(success.text)
            if "Thành công" in success.text:
                home = requests.get("https://vipig.net/home.php", cookies=self.cookie, headers=self.headvipig).text
                soduchinh = home.split('id="soduchinh">')[1].split('<')[0]
                useracc = home.split('Chào mừng <i>')[1].split('<')[0]
                print(success.json()["mess"]+","+" <> Xu:",soduchinh,","+" <> Tài khoản: "+useracc)
            else:
                print("Thất bại")

                
    def run(self):
        try:
            ua = UserAgent()
            ua = ua.chrome
        except:
            ua = "Mozilla/5.0 (Linux; Android 12; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.56 Mobile Safari/537.36"
        # ip = requests.get("http://ip-api.com/json", proxies=self.proxy).json()["query"]
        # print("IP:"+ip)
        self.headvipig = {
            "x-requested-with": "XMLHttpRequest",
            "content-type":"application/x-www-form-urlencoded; charset=UTF-8",}
        self.headers = {
            "x-ig-app-id": "1217981644879628",
            "x-asbd-id": "198387",
            # "x-ig-www-claim":self.www,
            "x-instagram-ajax": "c161aac700f",
            "accept": "*/*",
            "content-length": "0",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": ua,
            "x-csrftoken": self.cookieIg.split('csrftoken=')[1].split(';')[0],
            "x-requested-with": "XMLHttpRequest",
            "cookie": self.cookieIg.strip(),
        }
        self.head = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "cookie": str(self.cookieIg.strip()),
            "sec-ch-prefers-color-scheme": "dark",
            "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": ua,
            "viewport-width": "1366"
        }
        try:
            checkcookie = requests.get("https://www.instagram.com/chi2911ks/", headers=self.headers).text
            if "Login • Instagram" in checkcookie:
                print("Cookie Die")
                return
            check=self.dat_nick(self.cookieIg.split('ds_user_id=')[1].split(';')[0])
            if check=="dcm":
                print("Cookie die rồi")
                return
            #nv = random.choice(["like", "follow"])
            for nv in ["like", "follow"]:
                solan = likesolan if nv == "like" else  followsolan
                for job in range(solan):
                    checknv = self.getMission(nv)
                    if checknv == "no misson":
                        break
                    if checknv == "notblock":
                        break
                    elif checknv == "block":
                        break
                    elif checknv == "wait":
                        break
                    elif checknv == "hetjob":
                        break
        except Exception as e:
            pass


if exists("cookieig.txt") != True:
    open("cookieig.txt", "w+")
    inp = input("Nhập cookie :")
    open("cookieig.txt", "a+").write(input(inp)+"\n")
cookieIg = open("cookieig.txt").readlines()
if len(cookieIg) == 0:
    inp = input("Nhập cookie :")
    open("cookieig.txt", "a+").write(input(inp)+"\n")
user = input("Nhập tài khoản: ")
pwd = input("Nhập mật khẩu: ")
os.system('clear')
cookie = requests.post("https://vipig.net/login.php",data={"username": user,"password": pwd,"submit":"ĐĂNG+NHẬP"},headers={"content-type":"application/x-www-form-urlencoded"}, allow_redirects=False).cookies

delay_like = int(input("Delay like từ:"))
delay_like1 = int(input("đến:"))
delay_follow = int(input("Delay follow từ:"))
delay_follow1 = int(input("đến:"))
followsolan = int(input("Nhập số lần làm nhiệm vụ follow (lưu ý nhập 5 lần thì sẽ làm 25job):"))
likesolan = int(input("Nhập số lần làm nhiệm vụ like:"))
like_rand_delay = random.randint(delay_like, delay_like1)
follow_rand_delay = random.randint(delay_follow, delay_follow1)
if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")
while True:
    for ind in range(len(cookieIg)):
        cookieig = cookieIg[ind]
        if cookieig == "":
            continue
        ig = VipIg(cookie, cookieig,like_rand_delay, follow_rand_delay)
        ig.run()

