#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter="\t")

for entry in reader:
  author_id = entry[3]
  node_type = entry[5]
  # Ignore header
  if author_id == 'author_id':
    continue
  # If entry is a question, print its question id and author id
  if node_type == 'question':
    id = entry[0]
    print '{0}\t{1}'.format(id, author_id)
  # Else, print its the absolute question id and author id
  else:
    abs_parent_id = entry[7]
    print '{0}\t{1}'.format(abs_parent_id, author_id)

