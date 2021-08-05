#!/usr/bin/python
#Daniel Sanz Mayo

from pyspark import SparkConf, SparkContext
import sys
import string

conf = SparkConf().setMaster('local').setAppName('P4_spark')
sc = SparkContext(conf = conf)

RDDvar = sc.textFile("ratings.csv") #se crea un RDD
RDDvar2 = RDDvar.filter(lambda line: "userId" not in line)#para ignorar la primera fila del csv

datos = RDDvar2.map(lambda line: (int(line.split(',')[1]), float(line.split(',')[2]))) #cogemos los la pelicula y su valoracion
filas_peli = RDDvar2.map(lambda line: (int(line.split(',')[1]), 1))

#sumamos las valoraciones y el num de filas por cada peli para hacer la media
suma_val = datos.reduceByKey(lambda x,y: x + y)
suma_peli = filas_peli.reduceByKey(lambda x,y: x + y)

#unimos rdds
total = suma_val.join(suma_peli)

#media
resultado = total.map(lambda line: (line[0], float(line[1][0]/line[1][1])))

#rangos
r1 = resultado.filter(lambda line: line[1] <= 1.0).filter(lambda line: line[1] >= 0.0)
r2 = resultado.filter(lambda line: line[1] <= 2.0).filter(lambda line: line[1] > 1.0)
r3 = resultado.filter(lambda line: line[1] <= 3.0).filter(lambda line: line[1] > 2.0)
r4 = resultado.filter(lambda line: line[1] <= 4.0).filter(lambda line: line[1] > 3.0)
r5 = resultado.filter(lambda line: line[1] <= 5.0).filter(lambda line: line[1] > 4.0)

#un output por cada rango
r1.saveAsTextFile("output_P4_1.txt")
r2.saveAsTextFile("output_P4_2.txt")
r3.saveAsTextFile("output_P4_3.txt")
r4.saveAsTextFile("output_P4_4.txt")
r5.saveAsTextFile("output_P4_5.txt")

#Daniel Sanz Mayo
