#!/usr/bin/python
#Daniel Sanz Mayo
import sys
import re
import string

from pyspark import SparkConf, SparkContext


conf = SparkConf().setMaster('local').setAppName('P2_spark')
sc = SparkContext(conf = conf)

RDDvar = sc.textFile("access_log")
urls = RDDvar.map(lambda line: (line.split('"')[1], 1))

resultado = urls.reduceByKey(lambda a, b: a+b)
resultado_ord = resultado.sortByKey() #ordenar el resultado por orden alfabetico de URLs 

resultado_ord.saveAsTextFile("output_P2.txt")

    #Daniel Sanz Mayo

