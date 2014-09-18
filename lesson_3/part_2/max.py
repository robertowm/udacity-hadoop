#!/usr/bin/python

import sys

max = 0
key = None

for line in sys.stdin:
    data_mapped = line.strip()
    try:
        thisKey, thisValue = data_mapped.split("\t")

        if max <= float(thisValue):
            key = thisKey
            max = float(thisValue)
    except:
        print 'error'

print key, "\t", max

