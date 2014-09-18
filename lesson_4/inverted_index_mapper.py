#!/usr/bin/python

import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter="\t", quotechar='"')

for entry in reader:
  nodeId = entry[0]
  for word in re.compile(r'[\.\!\?\:;"\(\)\<\>\[\]#\$=\-/,\s]+').split(entry[4].strip()):
    if len(word) > 0:
      print "{0}\t{1}".format(word.lower(), nodeId)
