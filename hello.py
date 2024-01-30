from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from sys import stdout
 
class RestHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write('Hello World!')
        # optional: print a snippet of the request header to console
        print str(self.headers).replace('\r\n', ' ')[:120]; stdout.flush()
 
httpd = HTTPServer(('', 8000), RestHTTPRequestHandler)
while True:
    httpd.handle_request()
