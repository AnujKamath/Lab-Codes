from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, IntegerType, DoubleType

spark = SparkSession.builder \
    .appName("Kafka Integration") \
    .getOrCreate()

schema = StructType([
    StructField("lineID", IntegerType()),
    StructField("day", IntegerType()),
    StructField("pid", IntegerType()),
    StructField("adFlag", IntegerType()),
    StructField("availability", IntegerType()),
    StructField("competitorPrice", DoubleType()),
    StructField("click", IntegerType()),
    StructField("basket", IntegerType()),
    StructField("order", IntegerType()),
    StructField("price", DoubleType()),
    StructField("revenue", DoubleType())
])

kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "your_topic_name") \
    .load()

parsed_df = kafka_df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

existing_data_path = "data.csv" 
existing_data = spark.read.csv(existing_data_path, header=True, inferSchema=True)

query = parsed_df.writeStream \
    .outputMode("append") \
    .format("csv") \
    .option("path", existing_data_path) \
    .option("checkpointLocation", "path_to_checkpoint") \
    .start()

query.awaitTermination()
