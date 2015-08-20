#!/usr/bin/env python3

# CGI script redirects to a URL (from: redirect.cgi?url=URL) and increases the counter by 1

import cgi

COUNTER_FILE = "path/to/file"

form = cgi.FieldStorage()
if "url" in form:
	location = form['url'].value
	if location.find("://") == -1:
		location = "http://" + location
else:
	location = ""

if location:
	with open(COUNTER_FILE, "r+") as fp:
		counter = fp.read()
		if counter:
			counter = int(counter)
		else:
			counter = 0
		counter += 1
		fp.seek(0)
		fp.write(str(counter))
		fp.truncate()

print("Content-Type: text/html")
print("Status: 303 See Other")
print("Location: {}".format(location))
print()
