import http.server
import socketserver
from http import HTTPStatus
import logging
logger = logging.getLogger(__name__)

PORT=8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print('print')
        logger.info('Started')
        logger.warning('Finished')
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b'Hello World')

with socketserver.TCPServer(('', PORT), Handler) as httpd:
    httpd.serve_forever()
