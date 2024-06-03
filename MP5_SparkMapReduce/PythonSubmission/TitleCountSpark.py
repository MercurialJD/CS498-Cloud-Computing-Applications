#!/usr/bin/env python

'''Exectuion Command: spark-submit TitleCountSpark.py stopwords.txt delimiters.txt dataset/titles/ dataset/output'''

import sys
from operator import add
from pyspark import SparkConf, SparkContext

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]
stop_words, delimiters = [], []

with open(stopWordsPath) as f:
	#TODO
    for line in f:
        stop_words.append(line.strip())

with open(delimitersPath) as f:
    #TODO
    chars = f.read().rstrip('\n')
    for c in chars:
        delimiters.append(c)


def sort_schema(x):
    return x[0], -x[1]

def tokenize(text):
    tokens = []
    
    for d in delimiters:
        text = text.replace(d, ' ')
    text = text.lower().split()
    
    for word in text:
        if word not in stop_words:
            tokens.append(word)

    return tokens


conf = SparkConf().setMaster("local").setAppName("TitleCount")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

lines = sc.textFile(sys.argv[3], 1)

#TODO
res = lines.flatMap(lambda line: tokenize(line))\
            .map(lambda token: (token, 1))\
            .reduceByKey(add)\
            .top(10, key=lambda x: x[1])

res.sort(key=sort_schema)

outputFile = open(sys.argv[4],"w")

#TODO
#write results to output file. Foramt for each line: (line +"\n")
for x in res:
    outputFile.write("%s\t%d\n" % (x[0], x[1]))

outputFile.close()
sc.stop()
