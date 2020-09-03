from urllib.parse import urlencode
from urllib.request import urlopen, Request

#GET
http_response = urlopen('https://www.example.com')
#서버를 지정하자
body = http_response.read()
html = body.decode('cp949')

#POST

data = {
    'id' : 'b2her5',
    'pw' : '1234'
}


data=urlencode(data).encode('utf-8')

request = Request('https://nid.naver.com/nidlogin.login',data)
request.add_header('Content-Type', 'text/html')

http_response = urlopen(request)
body = http_response.read()
html = body.decode('utf-8')
print(html)