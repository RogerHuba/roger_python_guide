from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        message = "Hello World"
        self.wfile.write(message.encode())
        return

# This Python code defines a custom request handler class handler that inherits from BaseHTTPRequestHandler, and overrides the do_GET method to handle GET requests to the server.

# When a GET request is received by the server, the do_GET method is called and it performs the following actions:

# Sends a 200 OK response code to the client using the send_response method.
# Sets the Content-type header of the response to text/plain using the send_header method.
# Ends the headers using the end_headers method.
# Assigns a string "Hello World" to the message variable.
# Writes the message to the response body using the wfile.write method. This method writes bytes to the response body, so the string is first encoded to bytes using the encode method.
# This handler can be used to serve requests on a custom HTTP server that responds to GET requests with a plain text "Hello World" message.