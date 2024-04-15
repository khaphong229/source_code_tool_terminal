import requests, os

def short_link(link_key):
  api_token = '63a469a81f362c35c12f2d80'
  api_url = f"https://link4m.co/api-shorten/v2?api={api_token}&url={link_key}"
  result = requests.get(api_url).json()
  if result['status'] == 'error':
    print(result['message'])
  else:
    print(f"Link get key => {result['shortenedUrl']} ")

while True:
    link_key=input("Type a link: ")
    short_link(link_key)