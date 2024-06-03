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
# 5. Joining (10 points): The following program construct a new dataframe out of 'df' with a much smaller size.
####

# Now we are going to perform a JOIN operation on 'df2'. Do a self-join on 'df2' in lines with the same #'count1' values and see how many lines this JOIN could produce. Answer this question via DataFrame API and #Spark SQL API
# Spark SQL API
if __name__ == "__main__":
    sc = SparkContext()

    df = loadDataFrame(sc, "gbooks")
    df2 = df.select("word", "count1").distinct().limit(100);
    
    view_name = "gbooks2"
    value = runSparkSQL(sc, view_name, "SELECT count(1)\
                                        FROM {} AS g1\
                                        JOIN {} AS g2\
                                        ON g1.count1 = g2.count1".format(view_name, view_name), df2)
    
    print(value.first()['count(1)']) 
    sc.stop()

# output: 218
