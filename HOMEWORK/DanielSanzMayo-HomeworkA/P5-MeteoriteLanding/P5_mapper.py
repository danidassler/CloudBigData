#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    datos = re.split(r"\,", line)
    #el campo de la masa no siempre es el mismo
    #considero que si el campo de la masa está vacio no se cuenta, es decir como si no existiese (en total hay unos 525 meteoritos de 45716)
    if datos[4] != "": 
    	if datos[4][0] == " ": #si pasa esto entonces el campo de la masa es el 5 debido a que el 4 es el 2º argumento del tipo de meteorito dividido con una coma del campo 3 que es el 1er argumento del tipo de meteorito.
    		if datos[5] != "":
    			print(datos[3] +","+ datos[4] + '\t' + datos[5])
    	else:
    		print(datos[3] + '\t' + datos[4])
    		
    		
    		#Daniel Sanz Mayo
