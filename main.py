import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load CSV File
df = pd.read_csv("ecommerce_data.csv")

# Display first 5 rows
print("\nFirst 5 Records:")
print(df.head())

# Dataset Information
print("\nDataset Information:")
print(df.info())

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Select Features for Clustering
X = df[["AnnualIncome", "SpendingScore"]]

# Standardize Data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = kmeans.fit_predict(X_scaled)

# Display Clustered Data
print("\nCustomer Clusters:")
print(df[["CustomerID", "AnnualIncome", "SpendingScore", "Cluster"]])

# Save Result
df.to_csv("customer_segmented.csv", index=False)

print("\ncustomer_segmented.csv file saved successfully!")

# Scatter Plot
plt.figure(figsize=(8, 6))

plt.scatter(
    df["AnnualIncome"],
    df["SpendingScore"],
    c=df["Cluster"],
    s=100
)

plt.title("Customer Segmentation")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")

plt.show()
# data_loader
from data_loader import load_data, dataset_info

# Load Dataset
df = load_data()

# Display Information
dataset_info(df)
# DATA CLEANING 
from data_loader import load_data
from data_cleaning import clean_data

# Load Dataset
df = load_data()

# Clean Dataset
df = clean_data(df)

# Display first 5 rows
print(df.head())
# fetures_engineering
from data_loader import load_data
from data_cleaning import clean_data
from feature_engineering import feature_engineering

# Load data
df = load_data()

# Clean data
df = clean_data(df)

# Create new features
df = feature_engineering(df)

# Display updated data
print(df.head())
# rfm _analysis
from rfm_analysis import rfm_analysis

# RFM Analysis
rfm_df = rfm_analysis(df)

# Save Output
rfm_df.to_csv("rfm_analysis.csv", index=False)

print("\nRFM Analysis Completed Successfully!")
#SEGMENTION
from segmentation import customer_segmentation

# Customer Segmentation

df = customer_segmentation(df)

print(df.head())

# Save Output
df.to_csv("customer_segmented.csv", index=False)

print("Customer segmentation completed successfully.")
# visulization 
from visualization import (
    plot_age_distribution,
    plot_income_distribution,
    plot_spending_distribution,
    plot_customer_segments,
    plot_cluster_count
)

plot_age_distribution(df)
plot_income_distribution(df)
plot_spending_distribution(df)
plot_customer_segments(df)
plot_cluster_count(df)
