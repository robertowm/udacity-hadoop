#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    regexp = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) (.+) (.+) \[(.+)\] \"([A-Z]+) (.+) HTTP/.\..\" (.+) (.+)'
    match = re.match(regexp, line.strip())
    if match:
        ip, client, username, time, type, file, status, size  = match.groups()
        ### print "{0}\t{1}".format(ip, request)
        print ip
