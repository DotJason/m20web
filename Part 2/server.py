from http.server import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep


PORT_NUMBER = 8080


MIME_TYPES = {
    "html" : "text/html",
    "js" : "application/javascript",
    "css" : "text/css",
    "txt" : "text/plain"
}


def format(path):
    return path[path.rindex(".") + 1 :]


def format_mime_type(fmt):
    if fmt in MIME_TYPES:
        return MIME_TYPES[fmt]

    return None


def path_mime_type(path):
    return format_mime_type(format(path))


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"

        mime_type = path_mime_type(self.path)

        if mime_type is None:
            self.send_error(404, "File not found: " + self.path)
            return

        self.send_response(200)
        self.send_header("Content-type", mime_type)
        self.end_headers()

        file = open(curdir + sep + self.path)
        self.wfile.write(file.read().encode())
        file.close()

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
