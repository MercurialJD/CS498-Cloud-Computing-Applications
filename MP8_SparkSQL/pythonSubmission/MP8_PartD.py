from pyspark import SparkContext, SQLContext
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType, IntegerType

from MP8_PartA import loadDataFrame
from MP8_PartB import runSparkSQL


####
# 1. Setup (10 points): Download the gbook file and write a function to load it in an RDD & DataFrame
####

# RDD API
# Columns:
# 0: place (string), 1: count1 (int), 2: count2 (int), 3: count3 (int)


# Spark SQL - DataFrame API


####
# 4. MapReduce (10 points): List the three most frequent 'word' with their count of appearances
####

# Spark SQL
if __name__ == "__main__":
    sc = SparkContext()
    
    view_name = "tab_view"
    runSparkSQL(sc, view_name, "SELECT word, count(1)\
                                FROM {}\
                                GROUP BY word\
                                ORDER BY count(1) DESC".format(view_name)).show(n=3)
    
    sc.stop()

# There are 18 items with count = 425, so could be different 
# +---------+--------+
# |     word|count(1)|
# +---------+--------+
# |  all_DET|     425|
# | are_VERB|     425|
# |about_ADP|     425|
# +---------+--------+

