# clickstream-with-redpanda

# Clickstream Data Pipeline Project

This project simulates clickstream data generation, which is then sent to MinIO using Redpanda as the message broker. All components are containerized using Docker.

## Architecture

- **Clickstream Data Generator**: Simulates user interactions on a website and generates clickstream data.
- **Redpanda**: A high-performance streaming platform used to publish the clickstream data.
- **MinIO**: A high-performance, S3-compatible object storage used to store the processed data.

## Prerequisites

- Docker and Docker Compose installed on your machine.
- Basic knowledge of Docker and container orchestration.
