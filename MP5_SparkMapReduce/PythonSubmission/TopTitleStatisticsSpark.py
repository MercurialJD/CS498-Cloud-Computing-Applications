#!/usr/bin/env python
import sys
from math import floor
from pyspark import SparkConf, SparkContext

def mean(nums):
    return floor( sum(nums) / len(nums) )

def var(nums):
    mu = mean(nums)
    squared_diffs = [(n - mu) ** 2 for n in nums]
    return floor(sum(squared_diffs) / len(nums))

def getCount(line):
    token, cnt = line.split()
    return [cnt]

conf = SparkConf().setMaster("local").setAppName("TopTitleStatistics")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

lines = sc.textFile(sys.argv[1], 1)

#TODO
nums = lines.flatMap(lambda line: getCount(line)).collect()
nums = [int(n) for n in nums]

outputFile = open(sys.argv[2], "w")

#TODO write your output here
outputFile.write("Mean\t%s\n" % mean(nums))
outputFile.write("Sum\t%s\n" % sum(nums))
outputFile.write("Min\t%s\n" % min(nums))
outputFile.write("Max\t%s\n" % max(nums))
outputFile.write("Var\t%s\n" % var(nums))

outputFile.close()
sc.stop()
