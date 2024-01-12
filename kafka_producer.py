import csv
from kafka import KafkaProducer
import json

# Kafka configuration
broker = 'localhost:9092'
topic = 'stock-data'

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers=broker,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Read and send the CSV file
with open('D:/Hadoop/big-data/out.csv', encoding ='utf-8', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Send each row as a JSON message
        producer.send(topic, row)

# Ensure all messages are sent
producer.flush()

# Close the producer
producer.close()
