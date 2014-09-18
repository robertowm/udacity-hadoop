#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter="\t")

# If a tag needs a extra weight, it must be defined in the dict called 'weights'.
# The key must be the tag name and the value must be a value that will be printed.
weights = {}

for entry in reader:
  tagnames = entry[2]
  node_type = entry[5]
  # If entry is a question, print each tag with a count equals one
  if node_type == 'question':
    for tagname in tagnames.strip().split(' '):
      if tagname in weights:
        print tagname, '\t', weights[tagname]
      else:
        print tagname, '\t', 1
