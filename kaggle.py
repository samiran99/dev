import requests

# Remote file URL (you can change the month)
file_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet"

# Download file contents into a temporary location
local_path = "/tmp/yellow_tripdata_2023-01.parquet"

# Stream and save the file
with requests.get(file_url, stream=True) as r:
    with open(local_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

# Load into Spark DataFrame
df = spark.read.parquet(local_path)

# Preview the data
display(df)
