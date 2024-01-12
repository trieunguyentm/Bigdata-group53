from kafka import KafkaConsumer
from hdfs import InsecureClient
import json

# Kafka configuration
topic = 'stock-data'
broker = 'localhost:9092'

# HDFS configuration
hdfs_url = 'http://localhost:9870'
hdfs_path = '/vnstock-data'

# Create a Kafka consumer
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=[broker],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# Create an HDFS client
hdfs_client = InsecureClient(hdfs_url, user='root')

try:
    hdfs_client.status('/')
    print("success")
except Exception as e:
    print(f"error: {e}")

# Process messages
for message in consumer:
    data = message.value
    # Define the HDFS file path (you may want to include logic to create unique file names)
    file_path = f'{hdfs_path}/data-{message.offset}.json'

    try:
        print(data)
        with open('a.json', 'a') as file:
            json.dump(data, file, indent= 4)
            file.write("\n")
        hdfs_client.upload(f'{file_path}','a.json')
    except Exception as e:
        print(f"File successfully written to HDFS: {file_path}")



