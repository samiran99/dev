import requests

from pyspark.sql.functions import to_date, col

# NYC TLC Parquet file for January 2023
url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet"

# Load into Spark DataFrame
df = spark.read.parquet(url)

# Add a partition column (truncate datetime to date)
df = df.withColumn("pickup_date", to_date(col("tpep_pickup_datetime")))

# Preview
display(df.select("tpep_pickup_datetime", "pickup_date"))

# Preview the data
display(df)

# Save to Lakehouse Tables with partitioning
df.write.partitionBy("pickup_date") \
    .format("delta") \
    .mode("overwrite") \
    .save("Tables/nyc_taxi_partitioned")
