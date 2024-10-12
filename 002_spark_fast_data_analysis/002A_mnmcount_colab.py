from __future__ import print_function
import sys
from pyspark.sql import SparkSession

spark = (SparkSession
    .builder
    .appName("PythonMnMCount")
    .getOrCreate())

mnm_file = "/content/mnm_dataset.csv"

mnm_df = (spark.read.format("csv")
            .option("header", "true")
            .option("inferSchema", "true")
            .load(mnm_file))

mnm_df.show(n=5, truncate=False)

count_mnm_df = (mnm_df.select("State", "Color", "Count")
                .groupBy("State", "Color")
                .sum("Count")
                .orderBy("sum(Count)", ascending=False))

count_mnm_df.show(n=30, truncate=False)
print("Total Rows = %d" % (count_mnm_df.count()))

ca_count_mnm_df = (mnm_df.select("*")
                   .where(mnm_df.State == 'CA')
                   .groupBy("State", "Color")
                   .sum("Count")
                   .orderBy("sum(Count)", ascending=False))

ca_count_mnm_df.show(n=10, truncate=False)