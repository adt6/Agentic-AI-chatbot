import pandas as pd
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Generate Customers Data with Random Names
customers = pd.DataFrame({
    "customer_id": range(1, 51),
    "name": [fake.name() for _ in range(50)],  # Generate random names
    "postal_code": [random.randint(10000, 99999) for _ in range(50)],
    "email_address": [fake.email() for _ in range(50)],  # Generate random emails
    "home_address": [fake.address().replace("\n", ", ") for _ in range(50)],  # Generate realistic addresses
    "plan_id": [random.randint(1, 5) for _ in range(50)]  # Link each customer to a plan
})

# Generate Mobile Plans Data
mobile_plans = pd.DataFrame({
    "plan_id": range(1, 6),
    "plan_name": ["Basic Plan", "Standard Plan", "Premium Plan", "Family Plan", "Unlimited Plan"],
    "price": [20, 35, 50, 70, 90],
    "data_limit_GB": [5, 10, 25, 50, "Unlimited"],
    "talk_minutes": [500, 1000, "Unlimited", "Unlimited", "Unlimited"],
    "text_messages": ["Unlimited"] * 5
})

# Generate Devices Data
devices = pd.DataFrame({
    "device_id": range(1, 6),
    "device_name": ["Phone A", "Phone B", "Phone C", "Phone D", "Phone E"],
    "brand": ["BrandX", "BrandY", "BrandZ", "BrandX", "BrandY"],
    "price": [200, 400, 600, 800, 1000]
})

# Ensure every customer has a plan
customer_plans = pd.DataFrame({
    "customer_id": range(1, 51),
    "plan_id": [random.randint(1, 5) for _ in range(50)],
    "subscription_date": pd.date_range(start="2023-01-01", periods=50, freq="D"),
    "contract_duration_months": [random.choice([12, 24, 36]) for _ in range(50)],
    "auto_renewal": [random.choice([True, False]) for _ in range(50)]
})

# Ensure every customer has at least one device, some may have multiple
customer_device_entries = []
for customer_id in range(1, 51):
    num_devices = random.choice([1, 2])  # Some customers have 1 or 2 devices
    for _ in range(num_devices):
        customer_device_entries.append({
            "customer_id": customer_id,
            "device_id": random.randint(1, 5),
            "purchase_date": random.choice(pd.date_range(start="2023-06-01", periods=365)),
            "warranty_period_years": random.choice([1, 2, 3]),
            "insurance_opted": random.choice([True, False])
        })

# Convert to DataFrame
customer_devices = pd.DataFrame(customer_device_entries)

# Save CSV files
customers.to_csv("customers.csv", index=False)
mobile_plans.to_csv("mobile_plans.csv", index=False)
devices.to_csv("devices.csv", index=False)
customer_plans.to_csv("customer_plans.csv", index=False)
customer_devices.to_csv("customer_devices.csv", index=False)

print("CSV files have been generated successfully with random names and relationships!")
