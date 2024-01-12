from pyspark.sql import SparkSession

def main():
    # Tạo Spark Session
    # spark = SparkSession.builder\
    #     .appName("JsonToCassandra")\
    #     .config("spark.cassandra.connection.host", "cassandra")\
    #     .config("spark.cassandra.auth.username", "cassandra")\
    #     .config("spark.cassandra.auth.password", "cassandra")\
    #     .getOrCreate()

    spark = SparkSession. \
        builder. \
        appName("pyspark-notebook"). \
        master("spark://spark-master:7077"). \
        config("spark.executor.memory", "512m"). \
        getOrCreate()
    # spark = SparkSession.builder.appName("TestPySpark").getOrCreate()
    # print("PySpark is installed and SparkSession is created successfully.")

    df = spark.read.format("csv").option("header", "true").load("hdfs://namenode:9000/out.csv")
    df.show()


    # # Lưu DataFrame vào Cassandra
    # df.write\
    #   .format("org.apache.spark.sql.cassandra")\
    #   .mode("append")\
    #   .options(table="stock-data", keyspace="stock")\
    #   .save()
    #
    # spark.stop()

if __name__ == "__main__":
    main()
