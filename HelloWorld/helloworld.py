from http.server import BaseHTTPRequestHandler, HTTPServer


PORT_NUMBER = 8080


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        f = open("index.html")
        self.wfile.write(f.read().encode("utf-8"))
        f.close()

        return


def main():
    try:
        server = HTTPServer(('', PORT_NUMBER), Handler)
        print("Started server on port", PORT_NUMBER)
        server.serve_forever()
    except KeyboardInterrupt:
        print("Keyboard interrupt, shutting down server")
        server.socket.close()


if __name__ == '__main__':
    main()
