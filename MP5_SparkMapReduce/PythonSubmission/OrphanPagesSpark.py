#!/usr/bin/env python
import sys
from operator import or_
from pyspark import SparkConf, SparkContext

def hasParent(line):
    parent, children = line.strip().split(': ')

    ret = [(parent, False)]
    for child in children.split():
        ret.append((child, True))
    
    return ret

conf = SparkConf().setMaster("local").setAppName("OrphanPages")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

lines = sc.textFile(sys.argv[1], 1) 

#TODO
res = lines.flatMap(lambda line: hasParent(line))\
            .reduceByKey(or_)\
            .filter(lambda x: x[1] is False)\
            .collect()
            
res.sort(key=lambda x: x[0])

output = open(sys.argv[2], "w")

#TODO
#write results to output file. Foramt for each line: (line + "\n")
for x in res:    
    output.write("%s\n" % (x[0]))

output.close()
sc.stop()
