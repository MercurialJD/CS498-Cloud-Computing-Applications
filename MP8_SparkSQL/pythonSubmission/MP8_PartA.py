from pyspark import SparkContext, SQLContext
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType, IntegerType


####
# 1. Setup (10 points): Download the gbook file and write a function to load it in an RDD & DataFrame
####

# RDD API
# Columns:
# 0: place (string), 1: count1 (int), 2: count2 (int), 3: count3 (int)

# Spark SQL - DataFrame API
def loadDataFrame(sc, file_path='gbooks'):
    sqlContext = SQLContext(sc)

    def splitFunc(x):
        split_x = x.split()
        return split_x[0], int(split_x[1]), int(split_x[2]), int(split_x[3])

    rdd = sc.textFile(file_path).map(splitFunc)

    fields = [
        StructField("word", StringType(), True),
        StructField("count1", IntegerType(), True),
        StructField("count2", IntegerType(), True),
        StructField("count3", IntegerType(), True)
    ]
    df_schema = StructType(fields)

    df = sqlContext.createDataFrame(rdd, df_schema)
    return df


if __name__ == "__main__":
    sc = SparkContext()

    df = loadDataFrame(sc, "gbooks")
    df.printSchema()

    sc.stop()
