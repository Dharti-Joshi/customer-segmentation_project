import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Title

import streamlit as st

st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    layout="wide"
)

st.title("📊 Customer Segmentation Dashboard")

# Load Dataset
df = pd.read_csv("customer_segmented.csv")

# =========================
# KPIs
# =========================

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", len(df))
col2.metric("Average Income", f"₹{df['AnnualIncome'].mean():,.0f}")
col3.metric("Average Spending Score", round(df["SpendingScore"].mean(), 2))
col4.metric("Total Sales", f"₹{df['TotalSpent'].sum():,.0f}")

st.divider()

# =========================
# Dataset Preview
# =========================

st.subheader("Customer Data")
st.dataframe(df)

# =========================
# Customer Segment Count
# =========================

st.subheader("Customer Segments")

segment_count = df["CustomerSegment"].value_counts()

fig, ax = plt.subplots(figsize=(6,4))
ax.bar(segment_count.index, segment_count.values)

ax.set_xlabel("Segment")
ax.set_ylabel("Customers")

st.pyplot(fig)

# =========================
# Income vs Spending
# =========================

st.subheader("Income vs Spending Score")

fig, ax = plt.subplots(figsize=(7,5))

scatter = ax.scatter(
    df["AnnualIncome"],
    df["SpendingScore"],
    c=df["Cluster"]
)

ax.set_xlabel("Annual Income")
ax.set_ylabel("Spending Score")

st.pyplot(fig)

# =========================
# Age Distribution
# =========================

st.subheader("Age Distribution")

fig, ax = plt.subplots(figsize=(7,4))

ax.hist(df["Age"], bins=8)

ax.set_xlabel("Age")
ax.set_ylabel("Customers")

st.pyplot(fig)

# =========================
# Spending Score Distribution
# =========================

st.subheader("Spending Score Distribution")

fig, ax = plt.subplots(figsize=(7,4))

ax.hist(df["SpendingScore"], bins=8)

ax.set_xlabel("Spending Score")
ax.set_ylabel("Customers")

st.pyplot(fig)

# =========================
# Download Button
# =========================

st.download_button(
    label="Download Segmented CSV",
    data=df.to_csv(index=False),
    file_name="customer_segmented.csv",
    mime="text/csv"
)
#streamlit run dashboard.py
st.markdown("## 📌 Key Performance Indicators")

# Calculate KPI Values
total_customers = len(df)
total_sales = df["TotalSpent"].sum()
avg_income = df["AnnualIncome"].mean()
avg_spending = df["SpendingScore"].mean()
avg_age = df["Age"].mean()
avg_purchase = df["PurchaseFrequency"].mean()

# Display KPIs
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("👥 Total Customers", total_customers)

with col2:
    st.metric("💰 Total Sales", f"₹{total_sales:,.0f}")

with col3:
    st.metric("💵 Avg Annual Income", f"₹{avg_income:,.0f}")

col4, col5, col6 = st.columns(3)

with col4:
    st.metric("⭐ Avg Spending Score", f"{avg_spending:.1f}")

with col5:
    st.metric("🛒 Avg Purchase Frequency", f"{avg_purchase:.1f}")

with col6:
    st.metric("🎂 Avg Age", f"{avg_age:.1f} Years")

st.divider()
# python -m streamlit run dashboard.py run command