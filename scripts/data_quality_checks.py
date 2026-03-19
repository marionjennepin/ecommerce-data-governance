import pandas as pd
import re
import os

os.makedirs("reports", exist_ok=True)

customers = pd.read_csv("data/raw/customers.csv")
products = pd.read_csv("data/raw/products.csv")
orders = pd.read_csv("data/raw/orders.csv")

results = []

def add_result(table_name, rule_name, status, failed_count, comment):
    results.append({
        "table_name": table_name,
        "rule_name": rule_name,
        "status": status,
        "failed_count": failed_count,
        "comment": comment
    })

# -----------------------------
# Customers checks
# -----------------------------
failed = customers["customer_id"].isnull().sum()
add_result("customers", "customer_id_not_null", "PASS" if failed == 0 else "FAIL", failed, "Customer ID must not be null")

failed = customers["customer_id"].duplicated().sum()
add_result("customers", "customer_id_unique", "PASS" if failed == 0 else "FAIL", failed, "Customer ID must be unique")

email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
invalid_emails = customers["email"].fillna("").apply(lambda x: not bool(re.match(email_pattern, x))).sum()
add_result("customers", "email_valid_format", "PASS" if invalid_emails == 0 else "FAIL", invalid_emails, "Email must follow a valid format")

failed = customers["first_name"].isnull().sum()
add_result("customers", "first_name_not_null", "PASS" if failed == 0 else "FAIL", failed, "First name should not be null")

# -----------------------------
# Products checks
# -----------------------------
failed = products["product_id"].duplicated().sum()
add_result("products", "product_id_unique", "PASS" if failed == 0 else "FAIL", failed, "Product ID must be unique")

failed = (products["price"] <= 0).sum()
add_result("products", "price_positive", "PASS" if failed == 0 else "FAIL", failed, "Price must be strictly positive")

failed = products["category"].isnull().sum()
add_result("products", "category_not_null", "PASS" if failed == 0 else "FAIL", failed, "Category should not be null")

failed = (products["stock"] < 0).sum()
add_result("products", "stock_non_negative", "PASS" if failed == 0 else "FAIL", failed, "Stock cannot be negative")

# -----------------------------
# Orders checks
# -----------------------------
failed = orders["order_id"].duplicated().sum()
add_result("orders", "order_id_unique", "PASS" if failed == 0 else "FAIL", failed, "Order ID must be unique")

failed = (orders["quantity"] <= 0).sum()
add_result("orders", "quantity_positive", "PASS" if failed == 0 else "FAIL", failed, "Quantity must be greater than zero")

failed = (orders["total_amount"] < 0).sum()
add_result("orders", "total_amount_non_negative", "PASS" if failed == 0 else "FAIL", failed, "Total amount cannot be negative")

failed = orders["payment_method"].isnull().sum()
add_result("orders", "payment_method_not_null", "PASS" if failed == 0 else "FAIL", failed, "Payment method should not be null")

invalid_customers = (~orders["customer_id"].isin(customers["customer_id"])).sum()
add_result("orders", "customer_fk_valid", "PASS" if invalid_customers == 0 else "FAIL", invalid_customers, "Every customer_id in orders must exist in customers")

invalid_products = (~orders["product_id"].isin(products["product_id"])).sum()
add_result("orders", "product_fk_valid", "PASS" if invalid_products == 0 else "FAIL", invalid_products, "Every product_id in orders must exist in products")

report = pd.DataFrame(results)
report.to_csv("reports/data_quality_report.csv", index=False)

print(report)
print("\nData quality report saved to reports/data_quality_report.csv")