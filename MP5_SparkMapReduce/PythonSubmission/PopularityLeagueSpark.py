#!/usr/bin/env python

#Execution Command: spark-submit PopularityLeagueSpark.py dataset/links/ dataset/league.txt
import sys
from operator import add
from pyspark import SparkConf, SparkContext

def hasParent(line):
    parent, children = line.strip().split(': ')

    ret = [(parent, 0)]
    for child in children.split():
        ret.append((child, 1))
    
    return ret

conf = SparkConf().setMaster("local").setAppName("PopularityLeague")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

#TODO
lines = sc.textFile(sys.argv[1], 1)
link_cnt_map = lines.flatMap(lambda line: hasParent(line))\
                .reduceByKey(add)

#TODO
leagueIds = sc.textFile(sys.argv[2], 1)
leagueIds = leagueIds.collect()

#TODO
link_cnt_map = link_cnt_map.filter(lambda line: line[0] in leagueIds).collect()
counts = [int(cnt) for link, cnt in link_cnt_map]

link_cnt_map.sort(key=lambda x: x[0])
counts.sort()

output = open(sys.argv[3], "w")

#TODO
#write results to output file. Foramt for each line: (key + \t + value +"\n")
for link, cnt in link_cnt_map:
    output.write("%s\t%s\n" % (link, counts.index(cnt)))

output.close()
sc.stop()
