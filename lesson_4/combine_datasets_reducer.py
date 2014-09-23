#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys
import csv

def reducer():
  user_ptr_id = None
  aCode = None
  reputation = None
  gold = None
  silver = None
  bronze = None

  reader = csv.reader(sys.stdin, delimiter='\t')
  writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

  for line in reader:
    if line[1] == "A":
      user_ptr_id, aCode, reputation, gold, silver, bronze = line
    elif user_ptr_id != None:
      author_id, bCode, id, title, tagnames, node_type, parent_id, abs_parent_id, added_at, score = line
      if user_ptr_id == author_id:
        output = [id, title, tagnames, author_id, node_type, parent_id, abs_parent_id, added_at, score, reputation, gold, silver, bronze]
        writer.writerow(output)

reducer()