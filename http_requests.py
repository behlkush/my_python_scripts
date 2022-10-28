import requests

#simple script to display how get and post methods in http work in python

payload = {"firstName": "Rocky", "lastName": "TheMonster"}
req_response = requests.get("https://httpbin.org/get", params=payload)
print(req_response.status_code)
print(req_response.text)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
post_response = requests.post("https://httpbin.org/post", headers=headers, data=payload)
print(post_response.status_code)
print(post_response.text)
