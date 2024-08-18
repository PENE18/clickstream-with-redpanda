# clickstream-with-redpanda

# Clickstream Data Pipeline Project

This project integrates two primary data sources:
1. **MySQL Database**: Emulates the business's operational data, specifically focusing on user order transactions.
2. **Clickstream Data Generator**: Simulates user interactions on a website, producing clickstream events.

Both data sources are processed and sent to MinIO using Redpanda, a high-performance streaming platform. All components are containerized using Docker.

## Architecture

- **MySQL Database**: Stores user order transaction data, representing the core business operations.
- **Clickstream Data Generator**: Generates simulated clickstream events, such as page views and clicks.
- **Redpanda**: Serves as the message broker, handling the streaming of both MySQL data and clickstream events.
- **MinIO**: Provides S3-compatible object storage, where the processed data is stored.


## Prerequisites

- Docker and Docker Compose installed on your machine.
- Basic knowledge of Docker and container orchestration.
  
## 1. Running the Project
To start the entire stack, including MySQL, run the following command in the project root directory:
```bash
docker-compose --env-file .env up -d
```
Accessing MySQL
After starting the services, you can access the MySQL database directly from the Docker container using the following command:

```bash
docker exec -it mysql mysql -u"root" -p"${MYSQL_ROOT_PASSWORD}" ${MYSQL_DATABASE}
```

