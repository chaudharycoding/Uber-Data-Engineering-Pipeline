# Uber Data Engineering Pipeline

Welcome to my **Uber Data Engineering Pipeline** project! I designed the project to create a scalable and efficient data pipeline for processing and analyzing Uber data. The goal is to perform ETL (Extract, Transform, Load) on the data, making it ready for deeper analysis, visualizations, and insights.

## 🛠️ **Project Overview**

The project involves creating an end-to-end data pipeline that processes Uber's dataset of NYC taxi trips. Using a modern stack of cloud-based technologies and data engineering tools, where I aim to deliver a robust, scalable solution for Uber's data analysis needs.

---

## 📊 **Architecture**

The architecture of the pipeline is built using Google Cloud Platform (GCP) services to ensure scalability and flexibility in handling large datasets. I automated the pipeline using Mage.ai, which facilitates seamless data extraction, transformation, and then loading into BigQuery for analysis.

![Architecture](https://github.com/user-attachments/assets/cfecc8f2-955f-46ab-8f22-2ebf5c88e6a1)

---

## ⚙️ **Technology Stack**

- **Programming Language:** Python
- **Cloud Platform:** Google Cloud Platform (GCP)
  - Google Cloud Storage: For storing raw data.
  - Compute Instance: To run data processing scripts.
  - BigQuery: For analyzing the processed data.
  - Looker Studio: To visualize the data insights.
- **Pipeline Tool:** [Mage.ai](https://www.mage.ai/): A modern, intuitive tool to build and automate data pipelines.

---

## 📂 **Dataset Details**

- **Source:** [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- **Description:** The dataset includes detailed records of yellow and green taxi trips in NYC. The data covers:
  - Pick-up and drop-off times and locations.
  - Trip distance and fares.
  - Payment methods, rate types, and driver-reported passenger counts.
- **Dataset File:** [uber_data.csv](./uber_data.csv)
- **Data Dictionary:** [NYC TLC Data Dictionary](https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf)

---

## 💡 **Data Model**

The data model used in the project helps in transforming raw taxi trip records into actionable insights. Below is a visual representation of the data model:

![Data Model](Uber%20Data%20Model%20(1).svg)

---

## 📝 **SQL Queries**

SQL queries play a crucial role in transforming the raw data into a format suitable for analysis. This is the SQL file that I used for data transformation:

- [Query.sql](./Query.sql)

---

## 🐍 **Python Scripts**

- **ETL Script:** [load.py](./load.py) — This script is responsible for extracting the raw data, transforming it into the desired format, and loading it into the next steps of the pipeline.
- **BigQuery Load Script:** [load_bigquery.py](./load_bigquery.py) — This script uploads the transformed data into BigQuery for further analysis and querying.

---

## 📥 **Dataset Download**

Download the dataset used in this project here:

- [uber_data.csv](./data/uber_data.csv)

---

## 📚 **References**

- [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- [Mage Data Pipeline Tool](https://www.mage.ai/)


