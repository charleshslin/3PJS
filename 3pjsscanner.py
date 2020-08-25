#!/usr/bin/env python3.8
import urllib.request
import bs4

#Variables
srcs_selfhost = []
srcs_3p = []
violations = 0

#User input
URL = input("Provide URL to scan (without http://, https://, www.): ")

#Scan website
html = urllib.request.urlopen("http://" + URL).read()
soup = bs4.BeautifulSoup(html, features='html.parser')

#Scripts
scripts = soup.find_all('script')

for link in scripts:
	if 'src' in link.attrs:
		if link['src'] == "/" or URL in link['src']:
			srcs_selfhost.append(link['src'])
		elif 'integrity' in link.attrs:
			srcs_3p.append([link['src'], "yes"])
		else:
			srcs_3p.append([link['src'], "no"])

#Output
print(str(len(srcs_3p) + len(srcs_selfhost)) + " total scripts found")
print(str(len(srcs_selfhost)) + " self-hosted scripts found")
print(str(len(srcs_3p)) + " third-party scripts found")

for src in srcs_3p:
	if src[1] == "no":
		print(src[0] + " - NO SUBRESOURCE INTEGRITY FOUND")
		violations += 1
	else:
		print(src[0] + " - SUBRESOURCE INTEGRITY USED")

print(str(violations) + " VIOLATIONS FOUND")