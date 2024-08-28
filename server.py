from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000

class CustomHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

def run(server_class=HTTPServer, handler_class=CustomHandler):
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {PORT}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
