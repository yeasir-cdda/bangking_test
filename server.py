from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Send message back to client
        message = "Hello, World!"
        self.wfile.write(message.encode('utf-8'))
        return

def run():
    print('Starting server...')

    # Server settings
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, HelloRequestHandler)

    print('Server running on port 8000...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
