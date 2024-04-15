import requests

def link1s():
	link_key=input("Nhập link: ")
	api_token = 'e2972a7bea846ba97f94d72d2b95426481c5fe2e'
	api_url = f"https://traffic1s.com/api?api={api_token}&url={link_key}"
	result = requests.get(api_url).json()
	if result['status'] == 'error':
		print(result['message'])
	else:
		print(f"Link lấy key => {result['shortenedUrl']} ")

while True:
	link1s()
