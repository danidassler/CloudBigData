#!/usr/bin/python
#Daniel Sanz Mayo

from pyspark import SparkConf, SparkContext
import sys
import string

conf = SparkConf().setMaster('local').setAppName('P1_spark')
sc = SparkContext(conf = conf)

buscada = str(sys.argv[1]) #palabra a buscar, pasada como argumento
buscada_min = buscada.lower()

texto = sc.textFile("input.txt") #se crea un RDD (lineas del texto)
texto_min = texto.map(lambda line: line.lower())

result = texto_min.filter(lambda line: buscada_min in line)

result.saveAsTextFile("output_P1.txt")
           
           #Daniel Sanz Mayo
