import pandas as pd
import hashlib
import os

os.makedirs("data/curated", exist_ok=True)

customers = pd.read_csv("data/raw/customers.csv")
products = pd.read_csv("data/raw/products.csv")
orders = pd.read_csv("data/raw/orders.csv")

def hash_email(email):
    if pd.isna(email):
        return None
    return hashlib.sha256(email.encode()).hexdigest()

# -----------------------------
# Clean customers
# -----------------------------
customers_clean = customers.copy()

customers_clean = customers_clean.dropna(subset=["customer_id"])
customers_clean = customers_clean.drop_duplicates(subset=["customer_id"], keep="first")
customers_clean["first_name"] = customers_clean["first_name"].fillna("Unknown")
customers_clean["email_hash"] = customers_clean["email"].apply(hash_email)

# -----------------------------
# Clean products
# -----------------------------
products_clean = products.copy()

products_clean = products_clean.drop_duplicates(subset=["product_id"], keep="first")
products_clean = products_clean[products_clean["price"] > 0]
products_clean["category"] = products_clean["category"].fillna("Unknown")
products_clean["stock"] = products_clean["stock"].apply(lambda x: max(x, 0))

# -----------------------------
# Clean orders
# -----------------------------
orders_clean = orders.copy()

orders_clean = orders_clean.drop_duplicates(subset=["order_id"], keep="first")
orders_clean = orders_clean[orders_clean["quantity"] > 0]
orders_clean = orders_clean[orders_clean["total_amount"] >= 0]
orders_clean = orders_clean.dropna(subset=["payment_method"])

orders_clean = orders_clean[orders_clean["customer_id"].isin(customers_clean["customer_id"])]
orders_clean = orders_clean[orders_clean["product_id"].isin(products_clean["product_id"])]

# -----------------------------
# Enriched table
# -----------------------------
orders_enriched = (
    orders_clean
    .merge(customers_clean[["customer_id", "first_name", "last_name", "email_hash", "city", "country"]],
           on="customer_id", how="left")
    .merge(products_clean[["product_id", "product_name", "category", "price"]],
           on="product_id", how="left")
)

# Save outputs
customers_clean.to_csv("data/curated/customers_clean.csv", index=False)
products_clean.to_csv("data/curated/products_clean.csv", index=False)
orders_enriched.to_csv("data/curated/orders_enriched.csv", index=False)

print("Curated datasets generated in data/curated/")