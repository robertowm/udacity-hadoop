#!/usr/bin/python

import sys
import re
import urllib
import urlparse

for line in sys.stdin:
    regexp = '(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) (.+) (.+) \[(.+)\] \"([A-Z]+) (.+) HTTP/.\..\" (.+) (.+)'
    match = re.match(regexp, urllib.unquote(line.strip()))
    if match:
        ip, client, username, time, type, file, status, size  = match.groups()
        ## match = re.match('.+\.\w+' ,file)
        ## if match:
        # print re.sub('^(https?://.+)?/+', '/', file.split('?')[0]).lower()
        url = urlparse.urlparse(file)
        urlPath = url.path
        urlQuery = url.query
        if urlQuery: urlPath += '?' + urlQuery
        print urlPath
