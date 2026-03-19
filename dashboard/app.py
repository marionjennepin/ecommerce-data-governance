import streamlit as st
import pandas as pd

st.title("E-commerce Data Governance Dashboard")

kpis = pd.read_csv("reports/governance_kpis.csv")
dq = pd.read_csv("reports/data_quality_report.csv")
orders = pd.read_csv("data/curated/orders_enriched.csv")

st.header("Governance KPIs")
for _, row in kpis.iterrows():
    st.metric(row["kpi_name"], row["value"])

st.header("Data Quality Report")
st.dataframe(dq)

st.header("Orders by Status")
st.bar_chart(orders["status"].value_counts())

st.header("Revenue by Category")
revenue_by_category = orders.groupby("category")["total_amount"].sum().sort_values(ascending=False)
st.bar_chart(revenue_by_category)