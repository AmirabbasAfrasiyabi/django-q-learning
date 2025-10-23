import json
from email.utils import encode_rfc2231
from http.server import HTTPServer , BaseHTTPRequestHandler
from tkinter.font import names


class Profile(BaseHTTPRequestHandler):
    name:str
    age:int
    def __init__(self , name , age):
        self.name= name
        self.age = age


class ProfileEncoder(json.JSONEncoder):
    def default(self , obj):
        if isinstance(obj,Profile):
            return obj.__dict__
        return super().default(obj)

profile = Profile(None, None)

class MyRequestHandler(BaseHTTPRequestHandler):
    def _send_request(self,data,status,encoder = None):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data,cls=encoder).encode("utf8"))

    def do_GET(self):
        if self.path == '/hello':
            data = {'massage':'Helloworld'}
            self._send_request(data,200)
        if self.path == '/profile':
            data = profile
            self._send_request(data,200)
        else:
            self._send_request({'massage':'Not found'},404)

    def do_Put(self):
        if self.path == '/profile':
            content_lenght = int(self.headers.get('Content-Length'))
            request_body = self.rfile.read(content_lenght)
            print(f'request_body before load: {request_body}')
            request_body = json.loads(request_body)
            print(f'request_body after load: {request_body}')
            global profile
            profile.name = request_body['name']
            self.send_response({'massage':'OK'},201)

server = HTTPServer(('localhost', 8000), MyRequestHandler)
print('Started httpserver on port 8000')
server.serve_forever()

