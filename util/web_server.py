#-*- coding:utf-8 -*-

import http.server

host = '127.0.0.1'
port = 8000
httpd = http.server.HTTPServer((host, port), http.server.SimpleHTTPRequestHandler)
print('serving at port', port)
httpd.serve_forever()
