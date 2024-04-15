from codecs import unicode_escape_decode
import random, requests, os, platform, time, json, hashlib
import threading
from datetime import datetime
from md import *
listPr = []

def TmProxy(api_key: str):
    js={
        "api_key": api_key,
        "sign": "string",
        "id_location": 0
    }
    while(True):
        a=requests.post('https://tmproxy.com/api/proxy/get-new-proxy', json=js).json()
        if a['code']==0:
            return {'status': "success", 'http': a['data']['https']}
        elif a['code']==5:
            b=requests.post('https://tmproxy.com/api/proxy/get-current-proxy', json={'api_key': api_key}).json()
            if b['data']['timeout'] >= 300:
                return {'status': "success", 'http': b['data']['https']}
            else:
                giay=str(a['message']).split('after ')[1].split(' sec')[0]
                return {'status': "wait", 'time': giay}
        else:
            return {'status': "error", 'mess': a['message']}
    
def checkServer():
    a = requests.get("http://taimmo.net/server-free-test.php").json()
    if a['status'] == False:
        print(" \033[1;31mServer trải nghiệm đã hết hạn, vui lòng inbox admin để mua tool :))")
        time.sleep(100)
        exit()
    else:
        print(" \033[1;32mĐây là phiên bản trải nghiệm nhằm nâng cao độ ổn định tool :3")
        time.sleep(3)


class Instagram(object):
    def __init__(self, cookie: str) -> None:
        self.cookie = cookie
        self.xcsrftoken = cookie.split("csrftoken=")[1].split(';')[0]
    
    def setValues(self):
        try:
            headers = {
                'accept': "*/*",
                'authority': "www.instagram.com",
                'content-type': "application/x-www-form-urlencoded",
                'cookie': self.cookie,
                'user-agent': f"Mozilla/5.0 (Windows NT {random.choice(['7', '8', '10', '11'])}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90, 104)}.0.0.0 Safari/537.36",
                'x-csrftoken': self.xcsrftoken,
            }
            post = requests.get("https://www.instagram.com/", headers=headers).text
            self.idProfile = post.split('''"viewerId":"''')[1].split('"}')[0]
            self.x_instagram_ajax = post.split('''rollout_hash":''')[1].split('",')[0]
            self.appId = post.split('''"appId":"''')[1].split('","')[0]
            self.name = json.loads(unicode_escape_decode(post.split('full_name\\":')[1].split(',\\"')[0])[0])
            self.headersApi = {
                'accept': "*/*",
                'authority': "www.instagram.com",
                'content-type': "application/x-www-form-urlencoded",
                'cookie': self.cookie,
                'user-agent': f"Mozilla/5.0 (Windows NT {random.choice(['7', '8', '10', '11'])}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90, 104)}.0.0.0 Safari/537.36",
                'x-csrftoken': self.xcsrftoken,
                'x-requested-with': "XMLHttpRequest",
                'x-ig-app-id': self.appId,
                'x-instagram-ajax': self.x_instagram_ajax,
            }
        except:
            pass
    
    def getInfoCookie(self):
        try:
            try:
                id = self.idProfile
                name = self.name
            except:
                self.setValues()
                id = self.idProfile
                name = self.name
            return id, name
        except:
            pass
    def proxyAdd(self, proxy: str):
        self.proxyDict = { 
            "http"  : "http://{}".format(proxy), 
            "https" : "http://{}".format(proxy), 
        }

    def followUser(self, id: int, proxys = None) -> bool:
        try:
            if proxys != None:
                postFollow = requests.post(f"https://i.instagram.com/api/v1/web/friendships/{id}/follow/", headers=self.headersApi, proxies=self.proxyDict).json()
            else:
                postFollow = requests.post(f"https://i.instagram.com/api/v1/web/friendships/{id}/follow/", headers=self.headersApi).json()
            if postFollow['result'] == "following" and postFollow['status'] == "ok":
                return True
            else:
                return False
        except:
           return False 

    def likePost(self, id: int, proxys = None) -> bool:
        try:
            if proxys != None:
                postRec = requests.post("https://i.instagram.com/api/v1/web/likes/{}/like/".format(id), headers=self.headersApi, proxies=self.proxyDict).json()
            else:
                postRec = requests.post("https://i.instagram.com/api/v1/web/likes/{}/like/".format(id), headers=self.headersApi).json()
            if postRec['status'] == "ok":
                return True
            else:
                return False
        except:
           return False 

    def commentPost(self,id: int, text: str,proxys = None, *idReply) -> bool:
        try:
            if proxys != None:
                if idReply:
                    postCmt = requests.post(f"https://i.instagram.com/api/v1/web/comments/{id}/add/", data={'comment_text': text, 'replied_to_comment_id': str(idReply[0])}, headers=self.headersApi, proxies=self.proxyDict).json()
                else:
                    postCmt = requests.post(f"https://i.instagram.com/api/v1/web/comments/{id}/add/", data={'comment_text': text, 'replied_to_comment_id': ''}, headers=self.headersApi,proxies=self.proxyDict).json()
            else:
                if idReply:
                    postCmt = requests.post(f"https://i.instagram.com/api/v1/web/comments/{id}/add/", data={'comment_text': text, 'replied_to_comment_id': str(idReply[0])}, headers=self.headersApi).json()
                else:
                    postCmt = requests.post(f"https://i.instagram.com/api/v1/web/comments/{id}/add/", data={'comment_text': text, 'replied_to_comment_id': ''}, headers=self.headersApi).json()


            
            print(postCmt)
            if postCmt['status'] == "ok" and postCmt['text'] == text:
                return True
            else:
                return False
        except:
            return False
    
    def likeCmt(self, id: int, proxys = None) -> bool:
        try:
            if proxys != None:
                likeCmt = requests.post("https://www.instagram.com/web/comments/like/{}/".format(id), headers=self.headersApi, proxies=self.proxyDict).json()
            else:
                likeCmt = requests.post("https://www.instagram.com/web/comments/like/{}/".format(id), headers=self.headersApi).json()
            if likeCmt['status'] == "ok":
                return True
            else:
                return False
        except:
           return False 
        
    def upload_post(self):
        microtime = int(datetime.now().timestamp())

class TraoDoiSub(object):
    def __init__(self, token: str) -> None:
        self.token = token

    def loginTDS(self):
        a = requests.get("https://traodoisub.com/api/?fields=profile&access_token={}".format(self.token)).json()
        if "success" in a:
            return {'status': "success", 'data': {'user': a['data']['user'], 'xu': a['data']['xu']}}
        else:
            return {'status': "error", 'msg': "Sai tài khoản hoặc mật khẩu"}
    
    def getSoDu(self) -> dict:
        a = requests.get(f"https://traodoisub.com/api/?fields=profile&access_token={self.token}").json()
        if 'success' in a:
            return a['data']['xu']
        else:
            return 0

    def activeId(self, id: int) -> bool:
        apiActive = requests.get("https://traodoisub.com/api/?fields=instagram_run&id={}&access_token={}".format(id, self.token))
        if "success" in apiActive.text:
            return True
        else:
            return apiActive.json()['error']
        
    def getJob(self, typeJob: str) -> list:
        while(True):
            try:
                while(True):
                    a=requests.get('https://traodoisub.com/api/?fields={}&access_token={}'.format(typeJob, self.token)).json()
                    if 'fail_count' in a:
                        data = a['error'], False
                        break
                    if 'countdown' not in a:
                        data = a['data'], True
                        break
                    else:
                        pass
                return data
            except:
                pass
    
    def cacheJob(self, typejob: str, id: int) -> list:
        apiCache = requests.get("https://traodoisub.com/api/coin/?type={}&id={}&access_token={}".format(typejob, id, self.token)).json()
        if "success" in apiCache:
            data = apiCache['data']
            return {'status': "success", 'cache': data['cache'], 'xu_duyet': data['pending'], 'xu_cong': data['msg']}
        else:
            try:
                return {'status': "error", 'msg': apiCache['error']}
            except:
                return {'status': "error", 'msg': "Không xác định"}

def logo():
    print(" \033[1;32mAdmin:    \033[1;36mLê Tuấn Tài")
    print(" \033[1;32mYoutube:  \033[1;36mTài Lê Official")
    print(" \033[1;32mZalo:     \033[1;36m0398206564")
    print(" \033[1;32mFacebook: \033[1;36mtaile.official.2006")

def headInput(text: str):
    text = input(f"\033[1;31m [\033[1;32mTL\033[1;31m] \033[1;32m{text}: \033[1;33m")
    return text

def clear():
    os.system("cls" if platform.system() == "Windows" else 'clear')

def delay(text: str, delay: int):
    for x in range(int(delay), 0, -1):
        print(f"\033[1;31m [\033[1;32mTL\033[1;31m]\033[1;32m {text} {x} giây    ", end = "\r")
        time.sleep(1)

def changeIp(api_key, delay):
    while(True):
        listPr.clear()
        proxyNew = TmProxy(api_key)
        if proxyNew['status'] == "success":
            listPr.append(proxyNew['http'])
        time.sleep(delay*60+10)

listCookie = []
listJob = []
def app():
    x = 0
    while(True):
        x += 1
        cookieTikTok = headInput(f"Nhập Cookie Instagram Thứ {x}")
        
        if cookieTikTok == "":
            break
        else:
            listCookie.append(f"{cookieTikTok}")
            print(" "+"\033[1;37m="*36)
def main():
    clear()
    logo()
    print(" "+"\033[1;37m="*36)
    tokenTds = headInput("Nhập Token TraoDoiSub")
    tds = TraoDoiSub(tokenTds)
    login = tds.loginTDS()
    if login:
        user, xu = login['data']['user'], login['data']['xu']
    else:
        print("\033[1;31m Token TDS Không Hợp Lệ")
        exit(0)
    print(" "+"\033[1;37m="*36)
    if os.path.exists("cookie.txt") == False:
        open("cookie.txt", "w+")
    coo = open("cookie.txt", "r", encoding="utf-8-sig").read().split("\n")
    if len(coo) > 0:
        for ckText in coo:
            if len(ckText) > 15:
                listCookie.append(ckText)
        if len(listCookie) == 0:
            app()
    else:
        app()
    open("cookie.txt", "w+")
    for ckNe in listCookie:
        o = open("cookie.txt", "a+")
        o.write(ckNe+"\n")
        o.close()
    clear()
    logo()
    print(" "+"\033[1;37m="*36)
    delayJob = int(headInput("Nhập Delay Làm Nhiệm Vụ"))

    jobSleep = int(headInput("Sau bao nhiêu nhiệm vụ thì tạm nghỉ"))
    timeSleep = int(headInput(f"Sau \033[1;33m{jobSleep}\033[1;32m nhiệm vụ nghỉ bao nhiêu giây"))
    jobBreak = int(headInput(f"Đổi nick chạy sau bao nhiêu job"))
    print(" "+"\033[1;37m="*36)
    for typeJ in ['follow', 'like', 'cmt', 'likecmt']:
        job = headInput("Chạy job {} ?\033[1;31m(\033[1;33my\033[1;37m/\033[1;33mn\033[1;31m)".format(typeJ))
        if job == "y" or job == "Y":
            listJob.append(typeJ)
    print(" "+"\033[1;37m="*36)
    proxy = str(headInput("Muốn sử dụng proxy?\033[1;31m[\033[1;36m tmproxy.com\033[1;31m ] \033[1;31m[\033[1;36m Y/N\033[1;31m ]")).lower()
    if proxy == "y":
        keyProxy = str(headInput("Nhập API Key TmProxy"))
        delayProxy = int(headInput("Nhập thời gian đổi ip proxy"))
    print(" "+"\033[1;37m="*36)
    i = 0
    clear()
    logo()
    print(" "+"\033[1;37m="*36)
    print(f"\033[1;33m User TDS: {user}")
    print(f"\033[1;33m Tổng xu: {xu}")
    print(" "+"\033[1;37m="*36)
    if proxy == "y":
        threading.Thread(target=changeIp, args=(keyProxy,delayProxy,)).start()
    while(True):
        if len(listCookie) == 0:
            print("\033[1;31m Danh sách cookie hiện đã hết")
            app()
            open("cookie.txt", "w+")
            for ckNe in listCookie:
                o = open("cookie.txt", "a+")
                o.write(ckNe+"\n")
                o.close()
        for cookie in listCookie:
            jobError = 0
            jobNhanXu = 0
            ck = str(cookie)
            IG = Instagram(ck)
            idIg = IG.getInfoCookie()
            if idIg:
                idAccount, fullNameAccount = int(idIg[0]), idIg[1]
            else:
                print("\033[1;31m Cookie Die Hoặc Bị Chặn Requests")
                listCookie.remove(cookie)
                continue
            active = tds.activeId(idAccount)
            if active == True:
                print(f"\033[1;32m ID: \033[1;36m{idAccount} \033[1;37m| \033[1;32mTên Tài Khoản: \033[1;36m{fullNameAccount}")
                print(" "+"\033[1;37m="*36)
            else:
                print(active)
                continue
            while(True):
                jobRand = random.choice(listJob)
                if jobRand == "follow":
                    typeGet, typeCache, typeJobAction = "instagram_follow", "INS_FOLLOW_CACHE", "Follow"
                elif jobRand == "like":
                    typeGet, typeCache, typeJobAction = "instagram_like", "INS_LIKE_CACHE", "Like Post"
                elif jobRand == "cmt":
                    typeGet, typeCache, typeJobAction = "instagram_comment", "INS_COMMENT_CACHE", "Comment Post"
                elif jobRand == "likecmt":
                    typeGet, typeCache, typeJobAction = "instagram_likecmt", "INS_LIKECMT_CACHE", "Like Comment"
                chuyen = False
                getJob = tds.getJob(typeGet)
                if getJob[1] == False or getJob[0] == []:
                    continue
                for job in getJob[0]:
                    nextDelay = False
                    idCache = job['id']
                    idJob = str(job["id"]).split("_")[0]
                    if proxy == "y":
                        proxyAdd = listPr[0]
                        proxys = {
                            'http': "http://{}".format(proxyAdd),
                            'https': "http://{}".format(proxyAdd)
                        }
                        ip = requests.get("https://api.ipify.org/?format=json", proxies=proxys).json()['ip']
                        IG.proxyAdd(proxyAdd)
                    if jobRand == "follow":
                        postAction = IG.followUser(idJob, proxys=True if proxy == "y" else None)
                    elif jobRand == "like":
                        postAction = IG.likePost(idJob, proxys=True if proxy == "y" else None)
                    elif jobRand == "cmt":
                        postAction = IG.commentPost(idJob, proxys=True if proxy == "y" else None)
                    elif jobRand == "likecmt":
                        postAction = IG.likeCmt(idJob, proxys=True if proxy == "y" else None)
                    if postAction and postAction == True:
                        i += 1
                        jobNhanXu += 1
                        while(True):
                            cache = tds.cacheJob(typeCache, idCache)
                            if cache['status'] == "success":
                                jobError = 0
                                nextDelay = True
                                if proxy == "y":
                                    print(f"\033[1;31m [\033[1;32m{i}\033[1;31m] \033[1;32m<\033[1;31m+\033[1;32m> \033[1;31m[\033[1;36mTL\033[1;31m] \033[1;32m<\033[1;31m+\033[1;32m>\033[1;31m [\033[1;33m{ip}\033[1;31m]\033[1;31m [\033[1;33m{typeJobAction}\033[1;31m] \033[1;31m[\033[1;33m{idJob[0:8]}\033[1;31m] \033[1;32m<\033[1;31m+\033[1;32m> \033[1;33m{cache['xu_cong']} \033[1;32m<\033[1;31m+\033[1;32m>\033[1;32m Đợi Duyệt: \033[1;33m{cache['xu_duyet']}")
                                else:
                                    print(f"\033[1;31m [\033[1;32m{i}\033[1;31m] \033[1;32m<\033[1;31m+\033[1;32m> \033[1;31m[\033[1;36mTL\033[1;31m] \033[1;32m<\033[1;31m+\033[1;32m>\033[1;31m [\033[1;33m{typeJobAction}\033[1;31m] \033[1;31m[\033[1;33m{idJob[0:8]}\033[1;31m] \033[1;32m<\033[1;31m+\033[1;32m> \033[1;33m{cache['xu_cong']} \033[1;32m<\033[1;31m+\033[1;32m>\033[1;32m Đợi Duyệt: \033[1;33m{cache['xu_duyet']}")
                                break
                            time.sleep(2)
                    else:
                        jobError += 1
                        print("Follow Thất Bại", end = "\r")
                        if jobError >= 10:
                            print(jobError)
                            print(" "+"\033[1;37m="*36)
                            print(f"Tài khoản {fullNameAccount} bị chặn {typeJobAction}")
                            print(" "+"\033[1;37m="*36)
                            listCookie.remove(cookie)
                            chuyen = True
                            break
                    if jobNhanXu != 0 and jobNhanXu%int(jobBreak) == 0:
                        print(" "+"\033[1;37m="*36)
                        chuyen = True
                        break
                    if nextDelay == True:
                        if i%int(jobSleep) == 0:
                            delay("Nghỉ ngơi, chạy tiếp sau", int(timeSleep))
                        else:
                            delay("Làm nhiệm vụ tiếp theo sau", delayJob)
                if chuyen == True:
                    break

if (__name__ == "__main__"):    
    main()