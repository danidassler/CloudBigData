#!/usr/bin/python

import sys
import re

previous = None
sum = 0
doc_id =[]

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    key, value = line.split( '\t' )
    print (value)

#Daniel Sanz Mayo
