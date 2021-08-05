#!/usr/bin/python

import sys

previous = None
sum = 0
average = 0
count = 0

# necesario ejecutar con sort -n para que ordene bien los numeros

for line in sys.stdin:
    key, value = line.split( '\t' )

    if key != previous:
        if previous is not None:
            average = sum / count
            print (previous + '\t' + str(average))
        previous = key
        sum = 0
        count = 0
        
    count = count + 1
    sum = sum + float(value)
    
average=sum/count

print (previous + '\t' + str(average))

#Daniel Sanz Mayo
