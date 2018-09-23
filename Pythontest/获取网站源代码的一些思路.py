import requests
res = requests.get('https://www.baidu.com')
print (res.text.encode('utf-8'))