#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    buscada=sys.argv[1]
    line = re.sub( r'^\W+|\W+$', '', line )
    words = re.split(r"\W+", line)
    
    for word in words[1:]:
    	if word.lower() == buscada.lower():
           print(word.lower() + '\t' + line )
           
           #Daniel Sanz Mayo
