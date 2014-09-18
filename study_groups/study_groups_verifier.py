#!/usr/bin/python

import sys

expectedResult = [
  '111 	[100000066]',
  '15084 	[100004819]',
  '2 	[100000005]',
  '262 	[100004819]',
  '26454 	[100003192]',
  '3778 	[100000066, 100008254]',
  '6011204 	[100010128, 100020526, 100071170]',
  '6011936 	[100004819, 100019875, 100071170]',
  '6012754 	[100004819, 100012200]',
  '6015491 	[100004467, 100005156, 100071170]',
  '66193 	[100002460, 100004467, 100007808, 100071170]',
  '7185 	[100003268]',
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
      try:
        if sline[pos] != expectedResult[pointer][pos]:
          print '\tColumn: ', pos, ', "', sline[pos], '" != "', expectedResult[pointer][pos], '"'
      except:
        pass 
    print 'Expected: "', expectedResult[pointer], '"'
    print 'Input:    "', sline, '"'
    sys.exit(2)
  pointer += 1

if pointer < len(expectedResult):
  print 'Error, less lines than expected'
  sys.exit(3)

print 'Test passed!'

