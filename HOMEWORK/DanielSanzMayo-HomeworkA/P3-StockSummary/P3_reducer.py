#!/usr/bin/python

import sys

previous = None
sum = 0
average = 0
count = 0

for line in sys.stdin:
    key, value = line.split( '\t' )
    date = key.split('-')
    year = date[0]
    
    
    if year != previous:
        if previous is not None:
            average = sum / count
            print (previous + '\t' + str(average))
        previous = year
        sum = 0
        count = 0
        
    count = count + 1
    sum = sum + float(value)
    
average=sum/count

print (previous + '\t' + str(average))

#Daniel Sanz Mayo
