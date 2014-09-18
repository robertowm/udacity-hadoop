#!/usr/bin/python

import sys

oldWeekday = None
sum = 0
count = 0

def printline (key, value): print key, "\t", value
def printResult (weekday, sum, count):
  if sum == 0 or count == 0:
    printline(weekday, 0)
  else: 
    printline(weekday, (sum/count))

for line in sys.stdin:
  data = line.strip().split("\t")
 
  thisWeekday, thisPrice = data
  
  if oldWeekday == None:
    oldWeekday = thisWeekday

  if oldWeekday != thisWeekday:
    printResult(oldWeekday, sum, count)
    oldWeekday = thisWeekday
    sum = 0
    count = 0

  sum += float(thisPrice)
  count += 1

if oldWeekday != None:
  printResult(oldWeekday, sum, count)

