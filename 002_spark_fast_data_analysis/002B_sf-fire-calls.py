from pyspark.sql import SparkSession
from pyspark.sql.types import *

schema = StructType([
    StructField("CallNumber", IntegerType(), False),
    StructField("UnitID", StringType(), False),
    StructField("IncidentNumber", IntegerType(), False),
    StructField("CallType", StringType(), True),
    StructField("CallDate", StringType(), True),
    StructField("WatchDate", StringType(), True),
    StructField("CallFinalDisposition", StringType(), True),
    StructField("AvailableDtTm", StringType(), True),
    StructField("Address", StringType(), True),
    StructField("City", StringType(), True),
    StructField("Zipcode", IntegerType(), True),
    StructField("Battalion", StringType(), True),
    StructField("StationArea", StringType(), True),
    StructField("Box", StringType(), True),
    StructField("OriginalPriority", IntegerType(), True),
    StructField("Priority", IntegerType(), True),
    StructField("FinalPriority", IntegerType(), True),
    StructField("ALSUnit", BooleanType(), True),
    StructField("CallTypeGroup", StringType(), True),
    StructField("NumAlarms", IntegerType(), True),
    StructField("UnitType", StringType(), True),
    StructField("UnitSequenceInCallDispatch", IntegerType(), True),
    StructField("FirePreventionDistrict", IntegerType(), True),
    StructField("SupervisorDistrict", IntegerType(), True),
    StructField("Neighborhood", StringType(), True),
    StructField("Location", StringType(), True),
    StructField("RowID", StringType(), True),
    StructField("Delay", FloatType(), True)
])

spark = SparkSession.builder.appName("FireCalls").getOrCreate()

file_path = "/content/002B_sf-fire-calls.csv"
fire_df = spark.read.csv(file_path, header=True, schema=schema)

fire_df.show(5, truncate=False)

fire_df.printSchema()