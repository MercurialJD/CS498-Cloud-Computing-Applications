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
# 3. Filtering (10 points) Count the number of appearances of word 'ATTRIBUTE'
####

# Spark SQL
if __name__ == "__main__":
    sc = SparkContext()
    
    view_name = "tab_view"
    runSparkSQL(sc, view_name, "SELECT count(*)\
                                FROM {}\
                                WHERE word = \'ATTRIBUTE\'".format(view_name)).show()
    
    sc.stop()

# +--------+                                                                      
# |count(1)|
# +--------+
# |     201|
# +--------+


