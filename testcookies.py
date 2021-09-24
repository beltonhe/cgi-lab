#!/usr/bin/env python3
import os

print("Set-cookie: userID = abc;")
print("Set-cookie: passwprd = 123;")
print("Set-Cookie: expires: = Tuesday, 31-Dec-2007 23:12:40 GMT;")
print("Content-Type: text/html\r\n\r\n")
print("<html>")
print("head")
print("<body>")
print("<h2>All Done!</h2>")
print("<body>")
print("</html>")

for param in os.environ.keys():
    if param == "HTTP_COOKIE":
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))