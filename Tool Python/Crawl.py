from bs4 import BeautifulSoup
import requests


#CHECK LIVE AND GET INFO IG
def check_live_user(username: str) -> bool:
    URL = "https://www.instagram.com/{}/".format(username)
    out_put = BeautifulSoup(requests.get(URL).text, "html.parser")
    meta = out_put.find("meta", property ="og:description").attrs['content']
    data = {}
    crawl = meta.split("-")[0].split(" ")
    data['Followers'] = crawl[0]
    data['Following'] = crawl[2]
    data['Posts'] = crawl[4]
    return data

if (__name__ == "__main__"):
    followers, following, post = dict(check_live_user("nkhaphong")).items()
    print(followers)
    print(post)