#!/usr/bin/env python
import sys
from operator import add
from pyspark import SparkConf, SparkContext

def hasParent(line):
    parent, children = line.strip().split(': ')

    ret = [(parent, 0)]
    for child in children.split():
        ret.append((child, 1))
    
    return ret

conf = SparkConf().setMaster("local").setAppName("TopPopularLinks")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

lines = sc.textFile(sys.argv[1], 1) 

#TODO
res = lines.flatMap(lambda line: hasParent(line))\
            .reduceByKey(add)\
            .top(10, key=lambda x: x[1])

res.sort(key=lambda x: x[0])

output = open(sys.argv[2], "w")

#TODO
#write results to output file. Foramt for each line: (key + \t + value +"\n")
for x in res:    
    output.write("%s\t%d\n" % (x[0], x[1]))

output.close()
sc.stop()
