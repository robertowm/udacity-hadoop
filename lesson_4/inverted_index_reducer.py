#!/usr/bin/python

import sys

oldKey = None
sum = 0
nodes = []

for line in sys.stdin:
  data = line.strip().split("\t")
 
  thisKey, thisNode = data
  
  if oldKey == None:
    oldKey = thisKey

  if oldKey and oldKey != thisKey:
    print oldKey, "\t", sum, "\t", sorted(set(nodes))
    oldKey = thisKey
    sum = 0
    del nodes[:]

  sum += 1
  try:
    nodes.append(float(thisNode))
  except:
    nodes.append(-1)
if oldKey != None:
  print oldKey, "\t", sum, "\t", sorted(set(nodes))

