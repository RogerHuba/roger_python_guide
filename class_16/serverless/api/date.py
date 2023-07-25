# This Python code defines a custom request handler class handler that inherits from BaseHTTPRequestHandler, and overrides the do_GET method to handle GET requests to the server.
from http.server import BaseHTTPRequestHandler
from datetime import datetime

# BaseHTTPRequestHandler is a class in the http.server module of Python's standard library. It is a base class for implementing HTTP request handlers in Python web servers.

# This class has some methods that handle different HTTP request types such as GET, POST, PUT, DELETE, etc. and for sending response codes and headers to clients.

# When creating a custom HTTP server, you can create a subclass of BaseHTTPRequestHandler and override its methods to provide custom handling of HTTP requests. By default, BaseHTTPRequestHandler provides a basic implementation for each method that simply sends a response indicating that the request was not handled.

# This class is a useful starting point for building custom HTTP servers and implementing custom request handling logic.
class handler(BaseHTTPRequestHandler):

# When a GET request is received by the server, the do_GET method is called and it performs the following actions:
  def do_GET(self):
    
    # Sends a 200 OK response code to the client using the send_response method.
    self.send_response(200)

    # Sets the Content-type header of the response to text/plain using the send_header method.
    self.send_header('Content-type', 'text/plain')

    # Ends the headers using the end_headers method.
    self.end_headers()

    # Writes the current date and time in the format of "YYYY-MM-DD HH:MM:SS" to the response body using the wfile.write method. This method writes bytes to the response body, so the string is first encoded to bytes using the encode method.
    self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())

    # Returns from the method.
    return


# This handler can be used to serve requests on a custom HTTP server that responds to GET requests with the current date and time in plain text format.