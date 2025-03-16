import sqlite3
import pandas as pd
import os

# Define the path where your CSV files are stored
csv_path_datasets = "/Users/adityathakur/Desktop/Agentic AI/AI chatbot/datasets"
csv_path_database = "/Users/adityathakur/Desktop/Agentic AI/AI chatbot/database"

# Connect to SQLite database (creates a new one if it doesn't exist)
db_path = os.path.join(csv_path_database, "Telecom.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Load CSV files into Pandas DataFrames
customers = pd.read_csv(os.path.join(csv_path_datasets, "customers.csv"))
mobile_plans = pd.read_csv(os.path.join(csv_path_datasets, "mobile_plans.csv"))
devices = pd.read_csv(os.path.join(csv_path_datasets, "devices.csv"))
customer_plans = pd.read_csv(os.path.join(csv_path_datasets, "customer_plans.csv"))
customer_devices = pd.read_csv(os.path.join(csv_path_datasets, "customer_devices.csv"))

# Store DataFrames as SQLite tables
customers.to_sql("customers", conn, if_exists="replace", index=False)
mobile_plans.to_sql("mobile_plans", conn, if_exists="replace", index=False)
devices.to_sql("devices", conn, if_exists="replace", index=False)
customer_plans.to_sql("customer_plans", conn, if_exists="replace", index=False)
customer_devices.to_sql("customer_devices", conn, if_exists="replace", index=False)

# Commit and close connection
conn.commit()
conn.close()

print(f"CSV files have been successfully stored in SQLite database at {db_path}!")
