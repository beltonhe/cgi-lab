#!/usr/bin/env python3
import os
import json
print("content-type: text/html\r\n\r\n")
print
print("<title>Test CGI</title>")
print("<p>Hello World cmput 404 class!</p>")

print("environ")
print(os.environ)
json_object = json.dumps(dict(os.environ), indent = 4)
print("json obejct")
print(json_object)

print("question2")
for param in os.environ.keys():
    if (param=="QUERY_STRING"):
        print(f"<em>{param}</em> = {os.environ[param]}</li>")
        #print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))

print("question3")
for param in os.environ.keys():
    if (param=="HTTP_USER_AGENT"):
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))