import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def customer_segmentation(df):
    """
    Perform Customer Segmentation using K-Means Clustering.
    """

    print("\n========== CUSTOMER SEGMENTATION ==========")

    # Features for clustering
    features = [
        "AnnualIncome",
        "SpendingScore",
        "PurchaseFrequency",
        "TotalSpent"
    ]

    X = df[features]

    # Standardize data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # K-Means Model
    kmeans = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    # Create Cluster column
    df["Cluster"] = kmeans.fit_predict(X_scaled)

    # Segment Names
    segment_names = {
        0: "High Value",
        1: "Regular",
        2: "Premium"
    }

    df["CustomerSegment"] = df["Cluster"].map(segment_names)

    print("\nCluster Summary:")
    print(df["CustomerSegment"].value_counts())

    return df