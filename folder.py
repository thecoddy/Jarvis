#!/usr/bin/python3

print("content-type: text/html")
#print("location: https://www.google.com")
print()

import cgi 
import subprocess as sp
import os

form = cgi.FieldStorage()

folder = form.getvalue("FolderName")
os.system("mkdir /root/{0}".format(folder))
print("Folder named {} is created successfully...".format(folder))
