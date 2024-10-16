from pyspark.sql.types import *
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

schema = StructType([
   StructField("Id", IntegerType(), False),
   StructField("First", StringType(), False),
   StructField("Last", StringType(), False),
   StructField("Url", StringType(), False),
   StructField("Published", StringType(), False),
   StructField("Hits", IntegerType(), False),
   StructField("Campaigns", ArrayType(StringType()), False)])

data = [[1, "Jules", "Damji", "https://tinyurl.1", "1/4/2016", 4535, ["twitter", "LinkedIn"]],
       [2, "Brooke","Wenig","https://tinyurl.2", "5/5/2018", 8908, ["twitter", "LinkedIn"]],
       [3, "Denny", "Lee", "https://tinyurl.3","6/7/2019",7659, ["web", "twitter", "FB", "LinkedIn"]],
       [4, "Tathagata", "Das","https://tinyurl.4", "5/12/2018", 10568, ["twitter", "FB"]],
       [5, "Matei","Zaharia", "https://tinyurl.5", "5/14/2014", 40578, ["web", "twitter", "FB", "LinkedIn"]],
       [6, "Reynold", "Xin", "https://tinyurl.6", "3/2/2015", 25568, ["twitter", "LinkedIn"]]
      ]

if __name__ == "__main__":

   spark = (SparkSession
       .builder
       .appName("a")
       .getOrCreate())

   blogs_df = spark.createDataFrame(data, schema)
   blogs_df.show(truncate=False)
   print()

   blogs_df.printSchema()

    # expr() (expression) pozwala pisać wyrażenia SQL-owe w PySpark. W tym przypadku wyrażenie SQL to po prostu kolumna „Hits”.
   blogs_df.select(expr("Hits") * 2).show(2)
   blogs_df.select(col("Hits") * 2).show(2)
    # Ponownie używamy funkcji expr(), jednak tutaj całe wyrażenie „Hits * 2” jest traktowane jako wyrażenie SQL-owe.
   blogs_df.select(expr("Hits * 2")).show(2)

   blogs_df.withColumn("Big Hitters", (expr("Hits > 10000"))).show(truncate=False)
   blogs_df.printSchema()