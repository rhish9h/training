# 📘 Module 4: Messaging with Kafka

| Submodule                 | Study | Project | Difficulty |
| ------------------------- | ----- | ------- | ---------- |
| 4.1 Kafka Fundamentals    | 6h    | 3h      | I          |
| 4.2 Producers & Consumers | 5h    | 3h      | I–A        |
| 4.3 Error Handling & DLQ  | 4h    | 3h      | A          |

### 4.1 Kafka Fundamentals

| Item                 | Description                 | Learning Objectives                             | Micro-Project                         | Study | Build | Level |
| -------------------- | --------------------------- | ----------------------------------------------- | ------------------------------------- | ----- | ----- | ----- |
| 4.1.1 Kafka Concepts | Topics, partitions, brokers | - Understand Kafka's core architecture          | CLI-based Kafka topic publisher       | 2h    | 1h    | I     |
| 4.1.2 Setup & Config | Docker + CLI                | - Start broker, create topic                    | Local Kafka docker-compose file       | 2h    | 1h    | I     |
| 4.1.3 JSON Schemas   | Payload formats             | - Standardize schema across producers/consumers | Schema-validated weather event sender | 2h    | 1h    | I     |

**Branch Project 4.1:** Weather Streamer – Publish JSON-based weather data into Kafka topics with schema enforcement.

### 4.2 Producers & Consumers

| Item                     | Description           | Learning Objectives                   | Micro-Project                   | Study | Build | Level |
| ------------------------ | --------------------- | ------------------------------------- | ------------------------------- | ----- | ----- | ----- |
| 4.2.1 Async Producer     | Event generation      | - Batch writes, delivery confirmation | IoT sensor simulator            | 2h    | 1.5h  | I     |
| 4.2.2 Async Consumer     | Process stream data   | - Group coordination, offset commit   | Event stats aggregator          | 2h    | 1.5h  | I     |
| 4.2.3 Performance Tuning | Throughput & batching | - Configure buffer sizes, compression | High-volume publisher benchmark | 1h    | 1h    | A     |

**Branch Project 4.2:** Sensor Analytics Service – Full duplex Kafka pipeline with producer and consumer roles.

### 4.3 Error Handling & DLQ

| Item                 | Description                    | Learning Objectives     | Micro-Project                        | Study | Build | Level |
| -------------------- | ------------------------------ | ----------------------- | ------------------------------------ | ----- | ----- | ----- |
| 4.3.1 Retry Handling | Resilience to transient faults | - Retry with backoff    | Fault-tolerant consumer              | 2h    | 1.5h  | A     |
| 4.3.2 DLQ Strategy   | Dead Letter Queues             | - Store poison messages | DLQ handler for unprocessable events | 2h    | 1.5h  | A     |

**Branch Project 4.3:** Robust Event Processor – A resilient Kafka consumer that retries and reroutes broken messages to DLQ.

**Capstone 4:** IoT Event Stream Pipeline – Kafka-driven system with JSON sensors, DLQ strategy, fault-tolerant consumers, and observability hooks.
