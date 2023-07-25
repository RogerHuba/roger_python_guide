# This Python code defines a custom request handler class handler that inherits from BaseHTTPRequestHandler, and overrides the do_GET method to handle GET requests to the server.
from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

    # When a GET request is received by the server, the do_GET method is called and it performs the following actions:
    def do_GET(self):
        # Extracts the request path from the path attribute of the self object.
        s = self.path

        # Parses the query string of the request URL using parse.urlsplit and parse.parse_qsl functions from the urllib module, and creates a dictionary dic of the key-value pairs.
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        # Checks if the "word" parameter is present in the dictionary dic.
        # If the "word" parameter is present, sends a GET request to the dictionary API endpoint with the given word and retrieves the response data using the requests.get method.
        # Extracts the definition(s) of the word from the response data and appends them to a list definitions.
        # Converts the list definitions to a string and assigns it to the message variable.
        if "word" in dic:
            url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
            r = requests.get(url + dic["word"])
            data = r.json()
            definitions = []
            for word_data in data:
                definition = word_data["meanings"][0]["definitions"][0]["definition"]
                definitions.append(definition)
            message = str(definitions)

        # If the "word" parameter is not present, sets a message asking for a word to define.
        else:
            message = "Give me a word to define please"

        # Sends a 200 OK response code to the client using the send_response method.
        self.send_response(200)

        # Sets the Content-type header of the response to text/plain using the send_header method.
        self.send_header('Content-type','text/plain')

        # Ends the headers using the end_headers method.
        self.end_headers()

        # Writes the message to the response body using the wfile.write method. This method writes bytes to the response body, so the string is first encoded to bytes using the encode method.
        self.wfile.write(message.encode())

        return

# This handler can be used to serve requests on a custom HTTP server that responds to GET requests with the definition(s) of a given word obtained from an external dictionary API in plain text format.