#!/usr/bin/python

import sys

expectedResult = {
  '111 ': '111 	35 	0',
  '15084 ': '15084 	237 	0',
  '2 ': '2 	145 	0',
  '262 ': '262 	50 	0',
  '26454 ': '26454 	101 	0',
  '3778 ': '3778 	69 	164.0',
  '6011204 ': '6011204 	2651 	188.5',
  '6011936 ': '6011936 	347 	442.5',
  '6012754 ': '6012754 	369 	414.0',
  '6015491 ': '6015491 	170 	189.0',
  '66193 ': '66193 	60 	208.0',
  '7185 ': '7185 	86 	0'
}

count = 0

for line in sys.stdin:
  sline = line.strip()
  id, bodyLength, avgAnswersLength = sline.split('\t')
  if count >= len(expectedResult):
    print 'Error, more lines than expected'
    sys.exit(1)
  if id not in expectedResult:
    print 'Error, identifier not found: ', id
    print 'Line: ', sline
    sys.exit(2)
  if sline != expectedResult[id]:
    print 'Error in line ', count + 1
    for pos in range(0, len(sline) - 1):
      if sline[pos] != expectedResult[id][pos]:
        print '\tColumn: ', pos, ', "', sline[pos], '" != "', expectedResult[id][pos], '"' 
    print 'Expected: "', expectedResult[id], '"'
    print 'Input:    "', sline, '"'
    sys.exit(3)
  count += 1

if count < len(expectedResult):
  print 'Error, less lines than expected'
  sys.exit(4)

print 'Test passed!'

