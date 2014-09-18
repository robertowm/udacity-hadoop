#!/usr/bin/python

import sys
import csv
from datetime import datetime

## Convert a string to datetime
def toDatetime(date): 
  return datetime.strptime(date[:-3], '%Y-%m-%d %H:%M:%S.%f')

reader = csv.reader(sys.stdin, delimiter="\t")

for entry in reader:
  author_id = entry[3]
  added_at = entry[8]
  ## If we have an exception, ignore this entry.
  try:
    print '{0}\t{1}\t{2}'.format(author_id, toDatetime(added_at).hour, 1)
  except:
    pass
