# Introduction

![RedditDataEngineering](https://github.com/user-attachments/assets/8899c7c3-9690-4199-b40a-97a3adb1da27)

This project focuses on constructing a data pipeline that extracts data from Reddit and processes it using various AWS services. The architecture is designed to be both scalable and cost-effective, leveraging tools like Apache Airflow, AWS S3, AWS Glue, and AWS Redshift. The goal is to automate data extraction, transformation, and loading (ETL) processes while ensuring the data is easily accessible for analysis.

# System Architecture
Data Input
Sources: The data pipeline ingests data from Reddit using Python scripts managed by Apache Airflow.
Storage: Extracted data is initially stored in S3 buckets, categorized as Bronze Storage.
AWS Glue Crawler
Purpose: The Glue Crawler scans the S3 buckets to create a data catalog, making the data easily searchable and queryable in AWS services like Athena and Redshift.
Challenges: While powerful, Glue Crawlers have a minimum run time and lack event-driven triggers, which can be optimized by integrating with other AWS services.
AWS Lambda Function
Functionality: AWS Lambda functions are used to monitor the S3 bucket for new data and trigger the Glue Crawler. This ensures the data pipeline is event-driven, improving efficiency and reducing manual intervention.

# Modern System Architecture
Data Input: The data input remains the same, using Reddit data extracted through Python scripts managed by Apache Airflow.
Storage: Data is stored in a layered architecture in S3 (Bronze, Silver, Gold layers), facilitating different stages of data processing.
Processing: Data is processed using AWS Glue for ETL operations, transforming raw data into a refined format suitable for analysis.

# Implementation on AWS
1. Setting Up S3 Buckets
An S3 bucket named reddit-data-pipeline is created to store raw Reddit data (Bronze Layer). Additional buckets or folders can be set up for Silver and Gold layers as the data is transformed.
2. AWS Glue Crawler Configuration
The Glue Crawler is configured to scan the reddit-data-pipeline bucket and catalog the data into a database and tables. This allows for efficient querying of the data using AWS Athena or Redshift.
3. AWS Lambda Function Configuration
A Lambda function is created to trigger the Glue Crawler automatically when new data is uploaded to the S3 bucket. This makes the pipeline event-driven, ensuring that data is processed as soon as it is available.
4. Testing
The setup is tested by running the Airflow DAG to extract data from Reddit and upload it to the S3 bucket. The Lambda function triggers the Glue Crawler, which then updates the data catalog. The data is queried in Athena to ensure the process works as expected.
# Data Source
The pipeline uses Reddit data, specifically posts from a selected subreddit. This data includes fields such as post title, score, number of comments, author, and timestamps, providing a rich dataset for analysis.

# AWS Glue Crawler
The Glue Crawler is configured to scan the S3 bucket reddit-data-pipeline, cataloging the data into a structured format within a database. This setup ensures that data is ready for querying in services like AWS Athena or Redshift.

# S3 Bucket Structure
The S3 bucket reddit-data-pipeline is organized into layers:

Bronze Layer: Raw Reddit data is stored here immediately after extraction.
Silver Layer: Data is transformed and cleaned, making it ready for analysis.
Gold Layer: Final, highly curated data, optimized for specific business use cases.
# Conclusion
This project demonstrates the process of building a robust, scalable data pipeline using Reddit as a data source and AWS services for storage, processing, and querying. By automating the ETL process with Apache Airflow, AWS Lambda, and Glue Crawler, the architecture is both efficient and cost-effective, suitable for large-scale data engineering projects.


