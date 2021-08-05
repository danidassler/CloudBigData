#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    key, value = line.split( '\t' )
    value = value.strip("\n")
    print(value + '\t' + key)
    
    #Daniel Sanz Mayo
    
