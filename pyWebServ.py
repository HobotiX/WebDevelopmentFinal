#!C:\Python27\python.exe

import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()  ## This line enables CGI error reporting
 
server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8000)
#handler.cgi_directories = ["/cgi-bin"]
 
httpd = server(server_address, handler)
print "Server starting"
httpd.serve_forever()