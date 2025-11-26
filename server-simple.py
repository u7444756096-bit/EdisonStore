#!/usr/bin/env python3

import http.server
import socketserver
import os

os.chdir('/Users/imrancomoe/EdisonStore')

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        super().end_headers()

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    print(f"Open http://localhost:{PORT}/index.html in your browser")
    print("Press Ctrl+C to stop the server")
    httpd.serve_forever()
