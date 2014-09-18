#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter="\t")

for entry in reader:
  body = entry[4]
  node_type = entry[5]
  # If entry is a question, print its code, body length and code "A"
  if node_type == 'question':
    id = entry[0]
    print '{0}\tA\t{1}'.format(id, len(body))
  # If entry is an answer, print its parent code, body length and code "A"
  elif node_type == 'answer':
    abs_parent_id = entry[7]
    print '{0}\tB\t{1}'.format(abs_parent_id, len(body))

