#!/usr/bin/python

import sys

expectedResult = [
  '100000005 	1',
  '100000066 	1',
  '100000066 	5',
  '100002460 	12',
  '100003192 	8',
  '100003268 	15',
  '100004467 	12',
  '100004467 	20',
  '100004819 	4',
  '100005156 	17',
  '100007808 	12',
  '100008254 	22',
  '100010128 	14',
  '100012200 	5',
  '100019875 	5',
  '100020526 	14',
  '100071170 	5',
  '100071170 	12',
  '999999999 	9',
  '999999999 	12'
]

pointer = 0

for line in sys.stdin:
  if pointer >= len(expectedResult):
    print 'Error, more lines than expected'
    sys.exit(1)
  if line.strip() != expectedResult[pointer]:
    print 'Error in line ', pointer + 1
    print 'Expected: "', expectedResult[pointer], '"'
    print 'Input:    "', line.strip(), '"'
    sys.exit(2)
  pointer += 1

if pointer < len(expectedResult):
  print 'Error, less lines than expected'
  sys.exit(3)

print 'Test passed!'

