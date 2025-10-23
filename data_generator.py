from faker import Faker
import random
import uuid
from datetime import datetime

fake = Faker()

def generate_transaction():
    transaction = {
        "transaction_id": str(uuid.uuid4()),
        "user_id": random.randint(1000, 9999),
        "amount": round(random.uniform(5.0, 1000.0), 2),
        "product_category": random.choice(["Electronics", "Fashion", "Home", "Beauty", "Toys"]),
        "timestamp": datetime.utcnow().isoformat(),
        "ip_address": fake.ipv4_public(),
        "is_anomalous": random.choices([0, 1], weights=[98, 2])[0]
    }
    return transaction

if __name__ == "__main__":
    for _ in range(5):
        print(generate_transaction())
