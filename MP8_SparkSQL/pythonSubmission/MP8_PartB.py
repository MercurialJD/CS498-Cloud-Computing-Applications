from pyspark import SparkContext, SQLContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType, IntegerType

from MP8_PartA import loadDataFrame


####
# 1. Setup (10 points): Download the gbook file and write a function to load it in an RDD & DataFrame
####

# RDD API
# Columns:
# 0: place (string), 1: count1 (int), 2: count2 (int), 3: count3 (int)


# Spark SQL - DataFrame API

####
# 2. Counting (10 points): How many lines does the file contains? Answer this question via both RDD api & #Spark SQL
####

# Spark SQL
def runSparkSQL(sc, view_name, sql_cmd, df=None):
    if df is None:
        df = loadDataFrame(sc)
    
    df.createOrReplaceTempView(view_name)

    spark_session = SparkSession(sc)
    result = spark_session.sql(sql_cmd)
    
    return result


if __name__ == "__main__":
    sc = SparkContext()
    
    view_name = "tab_view"
    runSparkSQL(sc, view_name, "SELECT count(*)\
                                FROM {}".format(view_name)).show()
    
    sc.stop()

# +--------+                                                                              
# |count(1)|
# +--------+
# |86618505|
# +--------+


