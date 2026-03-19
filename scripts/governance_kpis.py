import pandas as pd
import os

os.makedirs("reports", exist_ok=True)

dq = pd.read_csv("reports/data_quality_report.csv")
customers_raw = pd.read_csv("data/raw/customers.csv")
products_raw = pd.read_csv("data/raw/products.csv")
orders_raw = pd.read_csv("data/raw/orders.csv")

customers_clean = pd.read_csv("data/curated/customers_clean.csv")
products_clean = pd.read_csv("data/curated/products_clean.csv")
orders_enriched = pd.read_csv("data/curated/orders_enriched.csv")

total_rules = len(dq)
passed_rules = (dq["status"] == "PASS").sum()
failed_rules = (dq["status"] == "FAIL").sum()
dq_success_rate = round((passed_rules / total_rules) * 100, 2)

raw_records = len(customers_raw) + len(products_raw) + len(orders_raw)
curated_records = len(customers_clean) + len(products_clean) + len(orders_enriched)
rejected_records = raw_records - curated_records

pii_fields_identified = 6
critical_tables = 3
monitored_tables = 3

kpis = pd.DataFrame([
    {"kpi_name": "total_rules", "value": total_rules},
    {"kpi_name": "passed_rules", "value": passed_rules},
    {"kpi_name": "failed_rules", "value": failed_rules},
    {"kpi_name": "dq_success_rate_pct", "value": dq_success_rate},
    {"kpi_name": "raw_records", "value": raw_records},
    {"kpi_name": "curated_records", "value": curated_records},
    {"kpi_name": "rejected_records", "value": rejected_records},
    {"kpi_name": "pii_fields_identified", "value": pii_fields_identified},
    {"kpi_name": "critical_tables", "value": critical_tables},
    {"kpi_name": "monitored_tables", "value": monitored_tables},
])

kpis.to_csv("reports/governance_kpis.csv", index=False)

print(kpis)
print("\nGovernance KPI file saved to reports/governance_kpis.csv")

