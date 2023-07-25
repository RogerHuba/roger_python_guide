from http.server import BaseHTTPRequestHandler
from urllib import parse
import platform

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        name = dic.get("name")

        if name:
            message = f"Aloha {name}"
        else:
            message = "Aloha stranger"

        message += f"\nGreetings from Python version {platform.python_version()}"
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

# This Python code defines a custom request handler class handler that inherits from BaseHTTPRequestHandler, and overrides the do_GET method to handle GET requests to the server.

# When a GET request is received by the server, the do_GET method is called and it performs the following actions:

# Extracts the request path from the path attribute of the self object.
# Parses the query string of the request URL using parse.urlsplit and parse.parse_qsl functions from the urllib module, and creates a dictionary dic of the key-value pairs.
# Retrieves the value of the "name" parameter from the dictionary dic using the get method, and assigns it to a variable name.
# If the "name" parameter is present, sets a personalized greeting message containing the value of the "name" parameter, otherwise sets a generic greeting message.
# Appends the Python version information to the greeting message using the platform.python_version() function.
# Sends a 200 OK response code to the client using the send_response method.
# Sets the Content-type header of the response to text/plain using the send_header method.
# Ends the headers using the end_headers method.
# Writes the greeting message to the response body using the wfile.write method. This method writes bytes to the response body, so the string is first encoded to bytes using the encode method.
# This handler can be used to serve requests on a custom HTTP server that responds to GET requests with a personalized greeting message containing the "name" parameter value (if present) and Python version information in plain text format.