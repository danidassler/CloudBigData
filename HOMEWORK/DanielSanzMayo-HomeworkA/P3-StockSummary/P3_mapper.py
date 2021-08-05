#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    datos = re.split(',', line)
    print(datos[0] + '\t' + datos[4])
    
    #Daniel Sanz Mayo
