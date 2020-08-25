#!/usr/bin/env python3.8
import urllib.request
import bs4

URL = input("Provide URL to scan: ")
html = urllib.request.urlopen("http://" + URL).read()
soup = bs4.BeautifulSoup(html, features='html.parser')
scripts = soup.find_all('script')
srcs = [link['src'] for link in scripts if 'src' in link.attrs]
print(srcs)