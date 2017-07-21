#!/usr/bin/python
print("Depois tentar esse tuto https://scotch.io/tutorials/build-your-first-python-and-django-application")
import SimpleHTTPServer
import SocketServer

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "Serving at port", PORT
httpd.serve_forever()