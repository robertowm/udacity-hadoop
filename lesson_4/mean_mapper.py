#!/usr/bin/python

import sys
from datetime import datetime

def toWeekday (weekday):
  if weekday == 0: return "Monday"
  elif weekday == 1: return "Tuesday"
  elif weekday == 2: return "Wednesday"
  elif weekday == 3: return "Thursday"
  elif weekday == 4: return "Friday"
  elif weekday == 5: return "Saturday"
  elif weekday == 6: return "Sunday"
  else: return weekday

for entry in sys.stdin:
  data = entry.strip().split("\t")
  price = data[4]
  date = data[0]
  weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
  print "{0}\t{1}".format(toWeekday(weekday), price)
