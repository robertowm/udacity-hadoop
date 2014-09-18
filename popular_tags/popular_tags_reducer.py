#!/usr/bin/python

import sys

# Represents how we define a tag.
class Tag:
  # Tag name
  name = None
  # Sum of weights
  sum = 0

  def __init__(self, name, weight):
    self.name = name
    self.sum = int(weight)

  # Add a new weight to this tag
  def addWeight(self, weight):
    self.sum += int(weight)

  # Print the result
  def printResult(self):
    print '{0}\t{1}'.format(self.name, self.sum)

tag = None

topN = 10
topList = []

def addToTopN(tag):
  global topList
  topList.append(tag)
  topList.sort(key=lambda t: t.name)
  topList.sort(key=lambda t: t.sum, reverse=True)
  if len(topList) > topN:
    topList = topList[:topN]

for line in sys.stdin:
  mappedData = line.strip().split("\t")
  if len(mappedData) != 2:
    # Something has gone wrong. Skip this line.
    continue
  
  # Load line to variables
  name, weight = mappedData
  
  if tag == None:
    tag = Tag(name, weight)
  elif tag.name == name:
    tag.addWeight(weight)
  else:
    addToTopN(tag)
    tag = Tag(name, weight)

# Add last tag to top list
if tag != None:
  addToTopN(tag)

for tag in topList:
  tag.printResult()
