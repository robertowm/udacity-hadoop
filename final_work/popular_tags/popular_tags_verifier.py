#!/usr/bin/python

import sys

expectedResult = [
  'cs101 	8',
  'cs253 	5',
  'discussion 	5',
  'issues 	3',
  'welcome 	3',
  'homework 	2',
  'jobs 	2',
  'lessons 	2',
  'meta 	2',
  'nationalities 	2'
]

pointer = 0

for line in sys.stdin:
  sline = line.strip()
  if pointer >= len(expectedResult):
    print 'Error, more lines than expected'
    sys.exit(1)
  if sline != expectedResult[pointer]:
    print 'Error in line ', pointer + 1
    for pos in range(0, len(sline) - 1):
      if sline[pos] != expectedResult[pointer][pos]:
        print '\tColumn: ', pos, ', "', sline[pos], '" != "', expectedResult[pointer][pos], '"' 
    print 'Expected: "', expectedResult[pointer], '"'
    print 'Input:    "', sline, '"'
    sys.exit(2)
  pointer += 1

if pointer < len(expectedResult):
  print 'Error, less lines than expected'
  sys.exit(4)

print 'Test passed!'

