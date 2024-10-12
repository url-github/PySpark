from pyspark.sql.types import *
from pyspark.sql.functions import *

schema = StructType([
   StructField("Id", IntegerType(), False),
   StructField("First", StringType(), False),
   StructField("Last", StringType(), False),
   StructField("Url", StringType(), False),
   StructField("Published", StringType(), False),
   StructField("Hits", IntegerType(), False),
   StructField("Campaigns", ArrayType(StringType()), False)])

if __name__ == "__main__":

   spark = (SparkSession
       .builder
       .appName("JSONDataExample")
       .getOrCreate())

   json_file = "/content/002B_blogs.json"

   blogs_df = spark.read.schema(schema).json(json_file)

   blogs_df.show(truncate=False)
   print()

   blogs_df.printSchema()

   blogs_df.select(expr("Hits") * 2).show(2)
   blogs_df.select(col("Hits") * 2).show(2)
   blogs_df.select(expr("Hits * 2")).show(2)

   blogs_df.withColumn("Big Hitters", expr("Hits > 10000")).show(truncate=False)

   blogs_df.printSchema()