from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import json
import ssl

# Elasticsearch authentication information
es_username = 'elastic'  # Replace with your actual Elasticsearch username
es_password = 'GNrDqIiRShS=8MOc-45H'  # Replace with your actual Elasticsearch password

# Initialize a Kafka consumer with multiple brokers
consumer = KafkaConsumer(
    'test_topic',
    bootstrap_servers=['localhost:9092', 'localhost:9093', 'localhost:9094'],
    auto_offset_reset='latest', # earliest
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# Initialize an Elasticsearch client
es = Elasticsearch(
    hosts=['https://localhost:9200'],
    http_auth=(es_username, es_password),
    verify_certs=False,
)

# Function to send data to Elasticsearch
def send_to_elasticsearch(data):
    try:
        res = es.index(index='test_index', body=data)  # Index each document
        print(f"Document indexed, ID: {res['_id']}")
    except Exception as e:
        print(f"Failed to index data: {e}")

# Process messages from Kafka
def process_messages():
    for message in consumer:
        try:
            data = message.value
            print(f"Type of data: {type(data)}")
            print(f"Received data: {data}")
            send_to_elasticsearch(data)
        except Exception as e:
            print(f"Failed read data: {e}")
            

if __name__ == "__main__":
    process_messages()
