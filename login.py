#!/usr/bin/env python3
import cgi, os, secret
from templates import secret_page

form = cgi.FieldStorage()

username = form.getvalue("username")
pwd = form.getvalue("password")


# set cookies
if secret.username == username and secret.password == pwd:
    print("Set-Cookie: userID = %s;" %username)
    print("Set-Cookie: Password = %s;" %pwd)

# search for the saved cookies 
for param in os.environ.keys():
    if param == "HTTP_COOKIE":
        cookies = os.environ[param]

cookie_username = ''
cookie_password = ''
cookies = cookies.split("; ")
for key in range(len(cookies)):
    block = cookies[key].split("=")
    if block[0] == "userID":
        cookie_username = block[1]
    if block[0] == "Password":
        cookie_password = block[1]

if secret.username == cookie_username and secret.password == cookie_password:
    print(secret_page(cookie_username, cookie_password))


print("content-type: text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program</title>")
print("</head>")
print("<body>")
print("<p><b>username:</b> %s<br><b>Password:</b>%s</p>" %(username, pwd))
print("</body>")
print("</html>")

