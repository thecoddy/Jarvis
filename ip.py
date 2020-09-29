#!/usr/bin/python3

print("content-type: text/html")
#print("location: https://www.google.com")
print()

import cgi 
import subprocess

#form = cgi.FieldStorage()

#x = form.getvalue("x")

op = subprocess.getoutput("ifconfig")
print(op)
