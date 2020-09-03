from http.server import BaseHTTPRequestHandler
class SimpleHTTPRequnestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print('ok!!!!!!!!!!!!!!!!!!!!!!')