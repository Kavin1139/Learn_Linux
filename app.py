from http.server import BaseHTTPRequestHandler, HTTPServer

class MyApp(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()

        self.wfile.write(b"Hello! My application is running.")

server = HTTPServer(("0.0.0.0", 8000), MyApp)
server.serve_forever()
