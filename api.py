from http.server import BaseHTTPRequestHandler, HTTPServer

class APIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"message": "GET request successful"}')

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        data = self.rfile.read(content_length)

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"message": "POST request received"}')

server = HTTPServer(("0.0.0.0", 8000), APIHandler)
server.serve_forever()
