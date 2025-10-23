from kafka import KafkaProducer
import json
import time
from data_generator import generate_transaction

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic_name = "transactions"

print("🚀 Kafka Producer started...")

while True:
    data = generate_transaction()
    producer.send(topic_name, value=data)
    print("Sent:", data)
    time.sleep(1)
