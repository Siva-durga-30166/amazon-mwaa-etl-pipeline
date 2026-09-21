# Amazon Managed Workflows for Apache Airflow Pipeline

## Project Code
24CC3014-P104

## Domain
Data Engineering

## Project Title
Amazon Managed Workflows for Apache Airflow Pipeline

## 1. Project Overview

This project is based on Data Engineering and focuses on building an ETL pipeline using Apache Airflow.

The project takes data from multiple CSV files, processes and transforms the data, and generates a final processed output file.

Apache Airflow is used to manage and execute the different stages of the ETL pipeline in the correct order.

The pipeline has been implemented and tested locally using Docker and Apache Airflow. The next step is to deploy the pipeline using Amazon MWAA.

## 2. Problem Statement

Data in real-world applications can come from different sources and may require multiple processing steps before it can be used.

Performing these steps manually can be difficult and time-consuming.

This project aims to solve this problem by creating an automated ETL pipeline and using Apache Airflow to manage the workflow and dependencies between the tasks.

## 3. Objectives

The main objectives of this project are:

- To create a multi-source ETL pipeline.
- To extract data from multiple CSV files.
- To combine and transform the data.
- To clean the data.
- To generate processed output data.
- To use Apache Airflow for workflow orchestration.
- To run and monitor the ETL pipeline.
- To prepare the pipeline for deployment on Amazon MWAA.

## 4. Data Sources

The project currently uses two CSV files.

### Sales Data

File:

`data/sales.csv`

It contains the following fields:

- sale_id
- customer_id
- product
- quantity
- price

### Customer Data

File:

`data/customers.csv`

It contains the following fields:

- customer_id
- customer_name
- city

## 5. ETL Process

The ETL process consists of three main stages.

### Extract

The sales and customer data are read from the CSV files using Python and Pandas.

### Transform

The two datasets are combined using `customer_id`.

The following transformations are performed:

- Calculate the total amount using quantity and price.
- Remove missing values.
- Convert customer names to uppercase.

The formula used is:

`total_amount = quantity * price`

### Load

The transformed data is saved as a CSV file.

The final output is:

`output/processed_sales.csv`

An intermediate transformed file is also created:

`output/transformed_sales.csv`

## 6. Python ETL

The Python ETL implementation is available in:

`src/etl.py`

The program performs the complete Extract, Transform and Load process.

The Python ETL pipeline was successfully executed and the processed output was generated.

## 7. Apache Airflow

Apache Airflow is used to orchestrate the ETL pipeline.

The DAG file is:

`dags/etl_pipeline.py`

The DAG name is:

`multi_source_etl_pipeline`

The DAG contains three tasks:

- extract_data
- transform_data
- load_data

The tasks are executed in the following order:

`extract_data -> transform_data -> load_data`

This ensures that each task is completed before the next task starts.

## 8. Docker Setup

Apache Airflow was configured using Docker.

The Docker configuration is available in:

`docker-compose.yaml`

Docker was used to create a local environment for running Apache Airflow on Windows.

The Airflow web interface was accessed using:

`http://localhost:8080`

## 9. Airflow Execution

The Airflow DAG was successfully triggered from the Airflow web interface.

All three tasks were executed successfully.

Execution result:

- extract_data - SUCCESS
- transform_data - SUCCESS
- load_data - SUCCESS
- DAG Run - SUCCESS

This confirms that the ETL workflow is working successfully with Apache Airflow in the local Docker environment.

## 10. Technologies Used

- Python
- Pandas
- Apache Airflow
- Docker
- Docker Compose
- Git
- GitHub
- CSV

AWS services such as Amazon S3 and Amazon MWAA will be used in the next phase of the project.

## 11. Project Structure

```text
airflow-etl-project/
│
├── data/
│   ├── sales.csv
│   └── customers.csv
│
├── output/
│   ├── processed_sales.csv
│   └── transformed_sales.csv
│
├── dags/
│   └── etl_pipeline.py
│
├── src/
│   └── etl.py
│
├── docker-compose.yaml
├── README.md
├── .gitignore
└── venv/