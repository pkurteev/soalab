from http.server import HTTPServer, BaseHTTPRequestHandler
from serializer import parse_json
import threading

json_answer = ''


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "//Ping":
            self.send_response(200)
            self.end_headers()
        elif self.path == "//Stop":
            self.send_response(200)
            self.end_headers()
            threading.Thread(target=httpd.shutdown).start()
        elif self.path == "//GetAnswer":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json_answer.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        global json_answer
        json_answer = parse_json(body.decode('utf-8'))
        self.send_response(200)
        self.end_headers()


if __name__ == '__main__':
    port = int(input())
    httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
