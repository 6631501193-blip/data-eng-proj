# Data Source & Ingestion Engineer – Starter Project

This project generates fake e-commerce transactions and streams them to Apache Kafka using Python.

## Setup
1. Install Docker & Python 3.9+
2. Start Kafka using Docker Compose:
   ```bash
   docker compose up -d
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4.   ```bash
   docker-compose up -d
   ```
4. Run the producer:
   ```bash
   python producer.py
   ```

## enerate Static Dataset
```bash
python generate_dataset.py
```

