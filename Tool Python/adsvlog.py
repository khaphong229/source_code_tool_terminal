import requests
import time, sys, os

def print_on_screen(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

introduce=('This is Tool AdsVlog by Python.\n\
Thank you for running my tool.\n\
Happy you good day.')
# print_on_screen(introduce)

auth='eyJhbGciOiJSUzI1NiIsImtpZCI6IjY5NjI5NzU5NmJiNWQ4N2NjOTc2Y2E2YmY0Mzc3NGE3YWE5OTMxMjkiLCJ0eXAiOiJKV1QifQ.eyJwcm92aWRlcl9pZCI6ImFub255bW91cyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9hZHN2bG9nLWJhY2tzdGFnZSIsImF1ZCI6ImFkc3Zsb2ctYmFja3N0YWdlIiwiYXV0aF90aW1lIjoxNzA3MTA3OTAxLCJ1c2VyX2lkIjoibFJOcEtMeTlIdmMyWEJiOG5UZVBxRlVWcDE0MyIsInN1YiI6ImxSTnBLTHk5SHZjMlhCYjhuVGVQcUZVVnAxNDMiLCJpYXQiOjE3MDcxMzg1MDIsImV4cCI6MTcwNzE0MjEwMiwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6e30sInNpZ25faW5fcHJvdmlkZXIiOiJhbm9ueW1vdXMifX0.MIQHqmjRkXOPmatxM3JwfosbTyuANmLA2mZ90vDcAC8c9z6aUNaZODu3SG09PRjnfis1dFVsc7DbQ5o-LoFY-7JmkqTZ0OAr3zkfdOp5WExr9W8paBNSOYX-1w2Tlange8FbgHuEof3kDv9ZCIKvn8LoWNV9YV6Euk6fikde2oF5x4DgvuCLCKEqfSJ1IXRy4CKosk9i-UOXgZ37tfJ9AQGz9ZUHWUkMgu6FRvR4deupszBmMioPTW7gnvAiodRvppiosmP0i85kMeTDsCClYSEpeQPfD5obW1dZi2jNBsShZN5K25FtJ0cVD_Eq7e1oH5ylhsjDfAlyrCeWHjMLxg'

# cki='_ga=GA1.1.2005503058.1707010823; _gcl_au=1.1.784404894.1707010836; _ga_3V5Q2KS7S0=GS1.1.1707106968.2.1.1707107156.0.0.0'
ua='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'

head_user={
    'host':'rest.backstage.adsvlog.com',
    'Authorization':auth,
    'Content-Type':'application/json',
    'User-Agent':ua,
}

head_receive={
    'host':'rest.backstage.adsvlog.com',
    'Authorization':auth,
    'content-length':'35',
    'Content-Type':'application/json',
    'performance-metrics':'eyJyZXF1aXJlZER1cmF0aW9uSW5TZWNvbmRzIjo5MiwidGltZVN0YW1wcyI6eyJsb2FkZWQiOjE3MDcxMzg2MDk2NTYsInN0YXJ0ZWQiOjE3MDcxMzg2NjgwNTcsImZpbmlzaGVkIjoxNzA3MTM4NzYwMDU5fX0=',
    'watching-metrics':'eyJwbGF5UGF1c2VCb251cyI6eyJyZWNlaXZlZCI6ZmFsc2V9LCJyZXdpbmRCb251cyI6eyJyZWNlaXZlZCI6ZmFsc2V9LCJjaGFuZ2VRdWFsaXR5Qm9udXMiOnsicmVjZWl2ZWQiOmZhbHNlfSwid2F0Y2hUaWxsRW5kQm9udXMiOnsicmVjZWl2ZWQiOmZhbHNlfX0=',
    'User-Agent':ua,
}

user=requests.get('https://rest.backstage.adsvlog.com/current-user/?locale=en&appId=com.adsvlog.getsubscribers&firebaseMessagingToken=&platforms=android,tablet,mobile,mobileweb&rtl=false&landscape=true&portrait=true&width=1067&height=528&last_visited_page=&app_build_date=2023-08-02T19:23:00Z&trackId=&referrerId=&geo=undefined',headers=head_user).json()
idUser=user['_id']
balance=user['balance']
print(f'Id user: {idUser} Balance: {balance}')

get_video=requests.get('https://rest.backstage.adsvlog.com/watch-earning/get-video/?locale=en&appId=com.adsvlog.getsubscribers&firebaseMessagingToken=&platforms=android,tablet,mobile,mobileweb&rtl=false&landscape=true&portrait=true&width=1067&height=528&last_visited_page=EarnWatching&app_build_date=2023-08-02T19:23:00Z&trackId=&referrerId=&geo=%7B%22country%22:%22Vietnam%22,%22timezone%22:%22Asia/Bangkok%22,%22organization%22:%22AS18403%20FPT%20Telecom%20Company%22,%22ip%22:%2242.118.57.128%22,%22asn%22:18403,%22area_code%22:%220%22,%22organization_name%22:%22FPT%20Telecom%20Company%22,%22country_code%22:%22VN%22,%22country_code3%22:%22VNM%22,%22continent_code%22:%22AS%22,%22latitude%22:%2221.0292%22,%22region%22:%22Hanoi%22,%22city%22:%22Hanoi%22,%22longitude%22:%22105.8526%22,%22accuracy%22:500%7D',headers=head_user).json()

urlVideo=get_video['url']
idVideo=get_video['youTubeVideoId']
idVideo2=get_video['_id']
reward=get_video['rewards']['base']

print(idVideo2)

for i in range(100,0,-1):
    print(f'please wait {i} seconds',end='\r')
    time.sleep(1)

data_receive={
    "adId":idVideo2,
}

receive=requests.post('https://rest.backstage.adsvlog.com/watch-earning/credit-video/?locale=en&appId=com.adsvlog.getsubscribers&firebaseMessagingToken=&platforms=android,tablet,mobile,mobileweb&rtl=false&landscape=true&portrait=true&width=1067&height=528&last_visited_page=EarnWatching&app_build_date=2023-08-02T19:23:00Z&trackId=&referrerId=&geo=%7B%22country%22:%22Vietnam%22,%22timezone%22:%22Asia/Bangkok%22,%22organization%22:%22AS18403%20FPT%20Telecom%20Company%22,%22ip%22:%2242.118.57.128%22,%22asn%22:18403,%22area_code%22:%220%22,%22organization_name%22:%22FPT%20Telecom%20Company%22,%22country_code%22:%22VN%22,%22country_code3%22:%22VNM%22,%22continent_code%22:%22AS%22,%22latitude%22:%2221.0292%22,%22region%22:%22Hanoi%22,%22city%22:%22Hanoi%22,%22longitude%22:%22105.8526%22,%22accuracy%22:500%7D',headers=head_receive,data={"adId":idVideo2})
# if receive['_id']==idVideo2:
#     print(f'SUCCESS {idVideo} {reward}')
# else:
#     print('FAIL')
print(receive)


