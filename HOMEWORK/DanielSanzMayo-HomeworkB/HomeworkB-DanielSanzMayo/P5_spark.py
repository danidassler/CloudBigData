#!/usr/bin/python
#Daniel Sanz Mayo

from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
import string
import sys
import re

conf = SparkConf().setMaster('local').setAppName('P5_spark')
sc = SparkContext(conf = conf)
ss = SparkSession(sc)

RDDvar = sc.textFile("Meteorite_Landings.csv") #se crea un RDD
lineas = RDDvar.flatMap(lambda line: line.split('\n')) #lineas del csv

sin_masa = lineas.map (lambda y: (re.split(r',(?! )', y)[3], re.split(r',(?! )', y)[4])).filter(lambda j: "" == j[1]) #meteoritos sin masa
con_masa = lineas.map (lambda y: (re.split(r',(?! )', y)[3], re.split(r',(?! )', y)[4])).filter(lambda j: "" != j[1]) #meteoritos con masa
sin_masa = sin_masa.map(lambda z: (z[0], 0)) #damos masa 0 a los meteoritos sin masa
todos = con_masa.union(sin_masa) #juntamos todos los meteoritos
todos_bueno = todos.map(lambda line: (line[0], float(line[1]))) #conversion importante a float para que funcionen las siguientes operaciones

df = todos_bueno.toDF(['tipo', 'masa']) #creamos el data-frame
media = df.groupBy('tipo').agg({'masa': 'mean'}) #hacemos la media
media.orderBy('tipo').show() #sacamos resultado por pantalla


#Daniel Sanz Mayo
