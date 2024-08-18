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
![System Diagram](https://github.com/PENE18/clickstream-with-redpanda/blob/main/screen/create.PNG)

Access the Data Generator
To generate transaction data for MySQL, access the data-generator container:

```bash
docker exec -it data_generator /bin/bash

```
mysql> select * from senegalese_ecommerce.olist_orders_dataset limit 10;
+----------------------------------+----------------------------------+--------------+--------------------------+---------------------+------------------------------+-------------------------------+-------------------------------+
| order_id                         | customer_id                      | order_status | order_purchase_timestamp | order_approved_at   | order_delivered_carrier_date | order_delivered_customer_date | order_estimated_delivery_date |
+----------------------------------+----------------------------------+--------------+--------------------------+---------------------+------------------------------+-------------------------------+-------------------------------+
| 004eab0fd8f28adaf8d488976f77febe | c476ddfbabfa4624603e0b7f8e245057 | delivered    | 2017-08-02 15:32:46      | 2017-08-02 15:45:17 | 2017-08-02 20:32:44    
      | 2017-08-03 18:17:47           | 2017-08-15 00:00:00           |
| 00b676b01c289cc661c6f7732492771a | ca9a6ae226341827c9614ce7568db46c | delivered    | 2017-08-02 15:30:42      | 2017-08-02 15:45:15 | 2017-08-08 15:37:43    
      | 2017-08-15 11:22:26           | 2017-08-24 00:00:00           |
| 011f9dff2545a2cf8ac1809faed3ec88 | fd10113c54f4f4bfcaacbd1c2d188a77 | delivered    | 2017-08-01 19:00:07      | 2017-08-01 19:10:21 | 2017-08-03 12:41:48    
      | 2017-08-09 21:04:42           | 2017-08-23 00:00:00           |
| 01c95de6d0852189b4d6b6d32a3c8e0c | 12a9f04e1b2cad4b8f510168f31d5663 | delivered    | 2017-08-03 23:13:48      | 2017-08-04 07:55:11 | 2017-08-07 12:52:11    
      | 2017-08-08 15:49:31           | 2017-08-16 00:00:00           |
| 01e4eeac4002b2e57b7ada6bc3a3c38f | 73b858b84d3afef2fdc6a26f3ee8c6f7 | delivered    | 2017-08-01 18:44:07      | 2017-08-01 18:55:11 | 2017-08-03 18:32:51    
      | 2017-08-08 20:33:42           | 2017-08-21 00:00:00           |
| 02ce6664223305cea5b46ef1f2d81461 | df3647cd1abeadb6a0fe143deb1b8cd2 | delivered    | 2017-08-02 21:25:06      | 2017-08-02 21:42:54 | 2017-08-03 18:29:42    
      | 2017-08-08 15:41:45           | 2017-08-22 00:00:00           |
| 030840d9a6c8137615d5a2c916667c2c | 677fbd5e154bdb06b0ad01bd85aa2ee3 | delivered    | 2017-08-01 14:40:53      | 2017-08-01 14:50:23 | 2017-08-02 19:17:02    
