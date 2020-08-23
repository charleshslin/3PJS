#!/usr/bin/env python3.8
import urllib.request

URL = input("Provide URL to scan: ")
html = urllib.request.urlopen("http://" + URL).read()
print(html)