import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta
import os

fake = Faker("fr_FR")
random.seed(42)
np.random.seed(42)

os.makedirs("data/raw", exist_ok=True)

# -----------------------------
# Customers
# -----------------------------
customers = []
for i in range(1, 201):
    customer_id = f"CUST{i:04d}"
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    city = fake.city()
    country = "France"
    signup_date = fake.date_between(start_date="-3y", end_date="today")
    birth_date = fake.date_between(start_date="-60y", end_date="-18y")
    phone = fake.phone_number()

    customers.append([
        customer_id, first_name, last_name, email, city, country,
        signup_date, birth_date, phone
    ])

customers_df = pd.DataFrame(customers, columns=[
    "customer_id", "first_name", "last_name", "email", "city", "country",
    "signup_date", "birth_date", "phone"
])

# Inject quality issues
customers_df.loc[5, "email"] = "invalid-email"
customers_df.loc[12, "email"] = None
customers_df.loc[25, "customer_id"] = customers_df.loc[24, "customer_id"]  # duplicate ID
customers_df.loc[40, "first_name"] = None
customers_df.loc[77, "phone"] = None

# -----------------------------
# Products
# -----------------------------
categories = ["Shoes", "Bags", "Accessories", "Jackets", "Jeans"]
products = []

for i in range(1, 51):
    product_id = f"PROD{i:03d}"
    product_name = f"{random.choice(categories)} Item {i}"
    category = random.choice(categories)
    price = round(random.uniform(10, 250), 2)
    stock = random.randint(0, 100)

    products.append([product_id, product_name, category, price, stock])

products_df = pd.DataFrame(products, columns=[
    "product_id", "product_name", "category", "price", "stock"
])

# Inject quality issues
products_df.loc[3, "price"] = -15.99
products_df.loc[10, "category"] = None
products_df.loc[20, "stock"] = -5

# -----------------------------
# Orders
# -----------------------------
orders = []
customer_ids = customers_df["customer_id"].tolist()
product_ids = products_df["product_id"].tolist()

for i in range(1, 501):
    order_id = f"ORD{i:05d}"
    customer_id = random.choice(customer_ids)
    product_id = random.choice(product_ids)
    quantity = random.randint(1, 5)
    order_date = fake.date_between(start_date="-1y", end_date="today")
    payment_method = random.choice(["Card", "PayPal", "Wire Transfer"])
    status = random.choice(["Completed", "Pending", "Cancelled"])

    product_price = float(products_df[products_df["product_id"] == product_id]["price"].iloc[0])
    total_amount = round(product_price * quantity, 2)

    orders.append([
        order_id, customer_id, product_id, quantity,
        order_date, payment_method, status, total_amount
    ])

orders_df = pd.DataFrame(orders, columns=[
    "order_id", "customer_id", "product_id", "quantity",
    "order_date", "payment_method", "status", "total_amount"
])

# Inject quality issues
orders_df.loc[7, "customer_id"] = "CUST9999"   # non-existing customer
orders_df.loc[18, "product_id"] = "PROD999"    # non-existing product
orders_df.loc[50, "quantity"] = 0
orders_df.loc[66, "total_amount"] = -120.0
orders_df.loc[80, "order_id"] = orders_df.loc[79, "order_id"]  # duplicate order_id
orders_df.loc[120, "payment_method"] = None

# Save files
customers_df.to_csv("data/raw/customers.csv", index=False)
products_df.to_csv("data/raw/products.csv", index=False)
orders_df.to_csv("data/raw/orders.csv", index=False)

print("Raw datasets generated in data/raw/")