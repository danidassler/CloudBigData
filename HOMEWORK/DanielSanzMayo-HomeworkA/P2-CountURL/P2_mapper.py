#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    words = re.split('"', line)
    print( words[1] + "\t1" )
    
    #Daniel Sanz Mayo

