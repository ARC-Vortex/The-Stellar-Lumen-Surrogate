from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Content-Type', 'application/javascript; charset=UTF-8' if self.path.endswith('.js') else 'text/html; charset=UTF-8')
        super().end_headers()

server = HTTPServer(('localhost', 8000), CustomHandler)
print("Serving at http://localhost:8000")
server.serve_forever()