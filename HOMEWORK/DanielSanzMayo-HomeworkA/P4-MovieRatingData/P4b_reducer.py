#!/usr/bin/python

import sys
import re



Rango1 = []
Rango2 = []
Rango3 = []
Rango4 = []
Rango5 = []

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    key, value = line.split( '\t' )

    if float(key) <= 1:
    	Rango1.append(value)
    elif float(key) > 1 and float(key) <= 2:
    	Rango2.append(value)
    elif float(key) > 2 and float(key) <= 3:
    	Rango3.append(value)
    elif float(key) > 3 and float(key) <= 4:
    	Rango4.append(value)
    elif float(key) > 4 and float(key) <= 5:
    	Rango5.append(value)

print ("Rango 1 --> " + ' ' + str(Rango1))
print ("Rango 2 --> " + ' ' + str(Rango2))
print ("Rango 3 --> " + ' ' + str(Rango3))
print ("Rango 4 --> " + ' ' + str(Rango4))
print ("Rango 5 --> " + ' ' + str(Rango5))


#Daniel Sanz Mayo
