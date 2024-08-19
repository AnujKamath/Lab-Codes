# from pyspark import SparkConf, SparkContext
# conf = SparkConf().setAppName("SquareNumbersApp").setMaster("local")
# sc = SparkContext(conf=conf)

# rdd = sc.parallelize([1, 2, 3, 4, 5])

# def square_it(num):
#     return num * num

# squares = rdd.map(square_it)
# result = squares.collect()
# print(result)

# sc.stop()
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def main():
    spark = SparkSession.builder \
        .appName("AddSquareColumn") \
        .master("local") \
        .getOrCreate()

    df = spark.read.csv("numbers.csv", header=True, inferSchema=True)

    print("Original DataFrame:")
    df.show()

    df_with_squares = df.withColumn("square", col("number") * col("number"))

    print("DataFrame with Squared Numbers:")
    df_with_squares.show()
    # df_with_squares.write.csv("numbers_with_squares.csv", header=True)

    spark.stop()

if __name__ == "__main__":
    main()
