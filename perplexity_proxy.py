#!/usr/bin/env python3
import http.server
import socketserver
import json

PORT = 8787

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ready"}).encode())

    def do_POST(self):
        if self.path == "/query":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"result": "Perplexity integration active"}
            self.wfile.write(json.dumps(response).encode())

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server running on port {PORT}")
    httpd.serve_forever()
