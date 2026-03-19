import pandas as pd

def anonymize_customer(customer_id):
    customers = pd.read_csv("data/curated/customers_clean.csv")
    orders = pd.read_csv("data/curated/orders_enriched.csv")

    mask = customers["customer_id"] == customer_id
    customers.loc[mask, "first_name"] = "ANONYMIZED"
    customers.loc[mask, "last_name"] = "ANONYMIZED"
    customers.loc[mask, "email"] = None
    customers.loc[mask, "phone"] = None

    mask_orders = orders["customer_id"] == customer_id
    orders.loc[mask_orders, "first_name"] = "ANONYMIZED"
    orders.loc[mask_orders, "last_name"] = "ANONYMIZED"

    customers.to_csv("data/curated/customers_clean.csv", index=False)
    orders.to_csv("data/curated/orders_enriched.csv", index=False)

    print(f"Customer {customer_id} anonymized in curated layer.")

def delete_customer(customer_id):
    customers = pd.read_csv("data/curated/customers_clean.csv")
    orders = pd.read_csv("data/curated/orders_enriched.csv")

    customers = customers[customers["customer_id"] != customer_id]
    orders = orders[orders["customer_id"] != customer_id]

    customers.to_csv("data/curated/customers_clean.csv", index=False)
    orders.to_csv("data/curated/orders_enriched.csv", index=False)

    print(f"Customer {customer_id} deleted from curated layer.")

if __name__ == "__main__":
    anonymize_customer("CUST0001")