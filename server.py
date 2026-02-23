import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", 8080))

Handler = http.server.SimpleHTTPServer

with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
