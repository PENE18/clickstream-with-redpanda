import json
import random
from datetime import datetime, timedelta
from faker import Faker
from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic
from time import sleep

# Kafka configuration
BOOTSTRAP_SERVERS = "redpanda:9092"
EVENTS_TOPIC_NAME = "test"

# Create Kafka admin client
admin_client = KafkaAdminClient(bootstrap_servers=BOOTSTRAP_SERVERS, client_id="test")

# Check if topic already exists, if not, create it
existing_topics = admin_client.list_topics()
if EVENTS_TOPIC_NAME not in existing_topics:
    print(f"Creating topic: {EVENTS_TOPIC_NAME}")
    admin_client.create_topics([NewTopic(EVENTS_TOPIC_NAME, num_partitions=1, replication_factor=1)])

# Create Kafka producer
producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS)

# Faker instance for generating mock data
fake = Faker()

# Mock data generation parameters
pages = ['home', 'product', 'search', 'cart', 'checkout']
actions = ['view', 'click', 'scroll', 'hover']
n_records = 5  # Number of records to generate

# Generate and send mock events
for _ in range(n_records):
    user_id = fake.uuid4()
    record = {
        "user_id": user_id,
        "name": fake.name(),
        "email": fake.email(),
        "age": fake.random_int(18, 70),
        "page": random.choice(pages),
        "action": random.choice(actions),
        "timestamp": (datetime.now() - timedelta(seconds=random.randint(0, 100000))).isoformat(),
        "session_id": random.randint(1, 10000),
        "duration": random.uniform(0.1, 10.0)  # Duration in seconds
    }
    
    # Convert record to JSON
    record_json = json.dumps(record)
    
    # Generate a key (example: user_id) for partitioning
    key = user_id.encode('utf-8')  # Using user_id as key (convert to bytes)
    
    # Send record to Kafka with key
    producer.send(EVENTS_TOPIC_NAME, key=key, value=record_json.encode('utf-8'))
    
    print(f"Sent data to Kafka topic {EVENTS_TOPIC_NAME} with key {user_id}: {record_json}")
    
    # Sleep for a short interval between sends (optional)
    sleep(3)

# Flush and close Kafka producer
producer.flush()
producer.close()
