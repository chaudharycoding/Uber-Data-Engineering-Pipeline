# Uber Data Engineering Pipeline

## Introduction
This project aims to create a scalable data engineering pipeline for Uber data using various tools and technologies. The primary goal is to perform ETL (Extract, Transform, Load) on the data for further analysis and visualization.

## Architecture
The architecture of the project follows a modern data engineering approach, leveraging cloud services and automation tools.

![Architecture]()
![architecture](https://github.com/user-attachments/assets/cfecc8f2-955f-46ab-8f22-2ebf5c88e6a1)

## Technology Stack
- **Programming Language:** Python
- **Cloud Platform:** Google Cloud Platform (GCP)
  - Google Storage
  - Compute Instance
  - BigQuery
  - Looker Studio
- **Pipeline Tool:** [Mage](https://www.mage.ai/)

## Dataset Used
- **Source:** [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- **Details:** The dataset contains yellow and green taxi trip records, including:
  - Pick-up and drop-off dates/times
  - Pick-up and drop-off locations
  - Trip distances
  - Itemized fares
  - Rate types, payment types, and driver-reported passenger counts.
- **Dataset File:** [uber_data.csv](./uber_data.csv)
- **Data Dictionary:** [NYC TLC Data Dictionary](https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf)

## Data Model
The following diagram represents the data model used in the project:

![Data Model](Uber%20Data%20Model%20(1).svg)

## SQL Query
The SQL query used for performing transformations on the data can be found in the following file:

- [Query.sql](./Query.sql)

## Python Scripts
- **ETL Script:** [load.py](./load.py) — This script handles the extraction and transformation of the data.
- **BigQuery Load Script:** [load_bigquery.py](./load_bigquery.py) — This script uploads the transformed data to BigQuery for analysis.

## Dataset Link
The dataset used in this project can be downloaded from: [uber_data.csv](./data/uber_data.csv)

## References
- [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- [Mage Data Pipeline Tool](https://www.mage.ai/)


