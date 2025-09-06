Medallion Architecture on Azure (From Zero to One)

This project implements a Medallion Architecture (Bronze → Silver → Gold) on Azure Databricks + Data Lake + ADF, using public data from Kaggle.

🚀 Project Steps

Kaggle Connector

Using the Kaggle API to ingest a public dataset.

Script: scripts/kaggle_to_bronze.py.

Ingestion (Bronze)

Raw data stored in ADLS Gen2 under the bronze container.

Notebook: 01_bronze_ingestao_churn.

Transformation (Silver)

Data cleaning, normalization, and type handling.

Notebook: 02_silver_tratamento_churn.

Presentation (Gold)

Data prepared for analytics and BI consumption.

Notebook: 03_gold_apresentacao_churn.

Governance & Permissions

Setup of IAM, RBAC, and Unity Catalog.

Access control for schemas and external locations.

Quotas & Compute

Cluster errors and quota adjustments faced during execution.

Orchestration (ADF)

Azure Data Factory pipeline calling Databricks notebooks.

File: pipelines/adf_pipeline.json.

Traceability (Purview)

Cataloging and lineage for full end-to-end visibility.

⚡ Key Learnings

Setting up roles and grants was crucial for enabling access.

Adjusting Azure compute quotas was necessary to avoid cluster failures.

Databricks ↔ ADF integration brought real orchestration to the workflow.

Each permission/quota error was part of the practical learning journey.

📊 Diagram

🔗 Dataset

Telco Customer Churn: Kaggle

📌 How to Reproduce

Clone the repository:

git clone https://github.com/youruser/medallion-azure-kaggle.git


Configure the Kaggle API (~/.kaggle/kaggle.json).

Set up Azure environment variables (.env).

Run the scripts and notebooks in order: Bronze → Silver → Gold.

Import the ADF pipeline.

👤 Author

Ronaldo Pereira
42 years | Data Architect & Data Engineer

LinkedIn

📧 ronaldooliveira499@gmail.com
