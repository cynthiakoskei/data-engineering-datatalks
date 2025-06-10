## An end-to-end data engineering project.

I am building an end-to-end data pipeline from scratch using modern data engineering tools and best practices. The project starts with setting up infrastructure on ` Google Cloud Platform (GCP)`  using ` Docker`  and ` Terraform`, including running ` PostgreSQL`  in containers. I’m using ` Kestra`  for workflow orchestration and managing data ingestion from APIs with a focus on scalability, data normalization and incremental loading. For storage and analytics, I use `BigQuery` where I apply partitioning, clustering and even with built-in ` machine learning`  features. I use ` dbt`  for analytics engineering to model, test and document data transformations in both ` PostgreSQL`  and ` BigQuery`. I visualize insights using Metabase dashboards. For batch processing, I work with Apache Spark to handle large datasets using DataFrames and ` Spark SQL`   and explore how groupBy and joins work internally. Finally, I implement real-time data streaming using ` Kafka` , ` Kafka Streams`  and ` KSQL`  and manage schemas using ` Avro`. This project helps me connect all stages of the data pipeline from ingestion to real-time and batch analytics.


<p align="center">
  <img width="100%" src="https://github.com/cynthiakoskei/data-engineering-datatalks/blob/main/Architecture%20Process.jpg" alt="Data Engineering Overview">
</p>


##  **Building an end-to-end data pipeline from scratch.**


### **Process**

#### [Stage 1: Containerization and Infrastructure as Code](01-docker-terraform/)
- GCP
- Docker and Docker Compose
- Running PostgreSQL with Docker
- Infrastructure setup with Terraform


#### [Stage 2: Workflow Orchestration](02-workflow-orchestration/)
- Data Lakes and Workflow Orchestration
- Workflow orchestration with Kestra


#### Sub-section: Data Ingestion
- API reading and pipeline scalability
- Data normalization and incremental loading


#### [Stage 3: Data Warehousing](03-data-warehouse/)
- BigQuery
- Partitioning, clustering and best practices
- Machine learning in BigQuery

#### [Stage 4: Analytics Engineering](04-analytics-engineering/)
- dbt (data build tool) with PostgreSQL & BigQuery
- Testing, documentation and deployment
- Data visualization with Metabase

#### [Stage 5: Batch Processing](05-batch/)
- Apache Spark
- DataFrames and SQL
- Internals of GroupBy and Joins

#### [Stage 6: Streaming](06-streaming/)
- Kafka
- Kafka Streams and KSQL
- Schema management with Avro


