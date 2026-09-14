\# Amazon Managed Workflows for Apache Airflow Pipeline



\## Project Code

24CC3014-P104



\## Domain

Data Engineering



\---



\# Project Overview



This project focuses on designing and implementing a Multi-Source ETL pipeline using Apache Airflow.



The pipeline extracts data from multiple sources, transforms and processes the data, and loads the processed data into an output layer.



The workflow is designed as an Apache Airflow DAG and can later be deployed using Amazon Managed Workflows for Apache Airflow (Amazon MWAA).



\---



\# Problem Statement



Data Engineering pipelines often involve multiple data sources and dependent processing tasks.



Managing these tasks manually can be difficult because:



\- Tasks have dependencies.

\- Data must be processed in the correct order.

\- Pipeline failures must be monitored.

\- Workflows need scheduling and automation.

\- Managing DAG dependencies across teams can become complex.



Apache Airflow provides workflow orchestration to manage these ETL processes.



\---



\# Objective



The objective of this project is to:



\- Build a multi-source ETL pipeline.

\- Extract data from multiple sources.

\- Transform and clean the extracted data.

\- Load processed data into an output layer.

\- Define the workflow using an Apache Airflow DAG.

\- Prepare the pipeline for future deployment using Amazon MWAA.



\---



\# ETL Workflow



Extract → Transform → Load



\## 1. Extract



The pipeline reads data from:



\- sales.csv

\- customers.csv



\## 2. Transform



The pipeline performs the following operations:



\- Merges sales and customer data.

\- Removes missing values.

\- Converts customer names to uppercase.

\- Calculates the total transaction amount.



Formula:



total\_amount = quantity × price



\## 3. Load



The processed data is saved as:



output/processed\_sales.csv



\---



\# Airflow DAG Workflow



The workflow is represented using an Apache Airflow DAG.



Extract Data

&#x20;    ↓

Transform Data

&#x20;    ↓

Load Data



The tasks are executed sequentially based on their dependencies.



\---



\# Project Architecture



Data Sources

&#x20;    │

&#x20;    ▼

sales.csv + customers.csv

&#x20;    │

&#x20;    ▼

Apache Airflow DAG

&#x20;    │

&#x20;    ▼

Extract

&#x20;    │

&#x20;    ▼

Transform

&#x20;    │

&#x20;    ▼

Load

&#x20;    │

&#x20;    ▼

Processed Output



\---



\# Technologies Used



\- Python

\- Pandas

\- Apache Airflow

\- ETL

\- CSV

\- Amazon MWAA (Planned)



\---



\# Current Implementation Status



| Component | Status |

|-----------|--------|

| Project Setup | Completed |

| Multi-Source Data | Completed |

| Extract Process | Completed |

| Transform Process | Completed |

| Load Process | Completed |

| Python ETL Pipeline | Working |

| Airflow DAG | Created |

| Local Airflow Execution | Pending |

| Amazon MWAA Deployment | Pending |



\---



\# Project Structure



```text

airflow-etl-project/

│

├── data/

│   ├── sales.csv

│   └── customers.csv

│

├── dags/

│   └── etl\_pipeline.py

│

├── output/

│   └── processed\_sales.csv

│

├── src/

│   └── etl.py

│

├── README.md

│

└── venv/

