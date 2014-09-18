#!/usr/bin/python

import sys

# Represents the control information that we will use.
class ControlData:
  # Key being processed
  key = None
  # Hour being processed
  hour = None
  # Accumulated counts
  accCount = 0
  # Max counts calculated
  maxCount = 0
  # List of hours with max counts
  maxHours = []

  def __init__(self, key, hour, accCount):
    self.key = key
    self.hour = hour
    self.accCount = float(accCount)

  # Update given a key, hour and its count
  def update(self, key, hour, count):
    # If accumulated count is bigger that max count found
    # then update max count and init the list of max hours
    if self.accCount > self.maxCount:
      self.maxCount = self.accCount
      self.maxHours[:] = [self.hour]
    # Else if accumulated count is equals to found max count
    # then append a new hour to list of max hours
    elif self.accCount == self.maxCount:
      self.maxHours.append(self.hour)

    self.initKeys(key, hour, count)

  # Initialize internal data given new input data
  def initKeys(self, key, hour, count):
    # If key changes, print content and initialize its variables
    if self.key != key:
      self.printContent()
      self.key = key
      self.maxCount = 0
      self.maxHours[:] = []
    # Update hour and accumulated count
    self.hour = hour
    self.accCount = float(count)

  # Print max hours given a key
  def printContent(self):
    for hour in sorted(self.maxHours):
      print self.key, '\t', hour

data = None

for line in sys.stdin:
  data_mapped = line.strip().split("\t")
  if len(data_mapped) != 3:
    # Something has gone wrong. Skip this line.
    continue
  
  # Load line to variables
  thisKey, thisHour, thisCount = data_mapped
  
  if data == None:
    # Create control data if it wasn't created
    data = ControlData(thisKey, thisHour, thisCount)
  elif data.key == thisKey:
    # If same key and hour, accumulate count
    if data.hour == thisHour:
      data.accCount += float(thisCount)
    # If same key but different hours, update control data 
    else:
      data.update(thisKey, thisHour, thisCount)
  else:
    # If different keys, update control data
    data.update(thisKey, thisHour, thisCount)

# Print last key
if data != None:
  data.printContent()
