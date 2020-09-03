from http.client import HTTPConnection

conn = HTTPConnection('www.example.com')


#GET / HTTP/1.1
#200 ok
conn.request('GET','/')
resp = conn.getresponse()
print(resp.status,resp.reason) #status 코드를 던진 이유 reason
#ok가 나왔으면은 아래 코드가 가능하다

if resp.status == 200:
    body = resp.read()
    print(body,type(body))


#실패
# GET /hello.html HTTP/1.1
#404 Not Found

conn.request('GET','/','hello.html')
