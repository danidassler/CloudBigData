#!/usr/bin/python
#Daniel Sanz Mayo

from pyspark import SparkConf, SparkContext
import sys
import string

conf = SparkConf().setMaster('local').setAppName('P3_spark')
sc = SparkContext(conf = conf)

RDDvar = sc.textFile("GOOGLE.csv") #se crea un RDD 
RDDvar2 = RDDvar.filter(lambda line: "Date" not in line) #para ignorar la primera fila del CSV

datos = RDDvar2.map(lambda line: (int(line.split(',')[0].split('-')[0]), float(line.split(',')[4]))) #cogemos anio y precio

filas_anio = RDDvar2.map(lambda line: (int(line.split(',')[0].split('-')[0]), 1)) #contamos cuantas filas hay por cada anio para porder hacer la media

#sumamos los precios y el num de filas por cada anio para hacer la media
suma_precios = datos.reduceByKey(lambda x,y: x + y)
suma_filas = filas_anio.reduceByKey(lambda x,y: x + y)

#unimos rdds
total = suma_precios.join(suma_filas)

#media
resultado = total.map(lambda line: (line[0], float(line[1][0]/line[1][1])))

resultado_ord = resultado.sortByKey() #ordenar el resultado por anio
resultado_ord.saveAsTextFile("output_P3.txt")

#Daniel Sanz Mayo

