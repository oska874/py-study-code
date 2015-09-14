# web lib request test
import requests

r = requests.get('http://baidu.com')
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)

r = requests.post("http://httpbin.org/post")

print(r.status_code)