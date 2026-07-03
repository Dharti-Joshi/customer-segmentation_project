import pandas as pd

def clean_data(df):
    """
    Clean the customer dataset.
    """

    print("\n========== Data Cleaning Started ==========")

    # Remove duplicate rows
    duplicates = df.duplicated().sum()
    print(f"Duplicate Records: {duplicates}")

    if duplicates > 0:
        df = df.drop_duplicates()

    # Check missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Fill missing numeric values with median
    numeric_columns = [
        "Age",
        "AnnualIncome",
        "SpendingScore",
        "PurchaseFrequency",
        "TotalSpent"
    ]

    for col in numeric_columns:
        if df[col].isnull().sum() > 0:
            df[col] = df[col].fillna(df[col].median())

    # Fill missing Gender values with mode
    if df["Gender"].isnull().sum() > 0:
        df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])

    # Remove negative values
    df = df[
        (df["Age"] > 0) &
        (df["AnnualIncome"] >= 0) &
        (df["SpendingScore"] >= 0) &
        (df["PurchaseFrequency"] >= 0) &
        (df["TotalSpent"] >= 0)
    ]

    print("\n========== Data Cleaning Completed ==========")
    print("Final Dataset Shape:", df.shape)

    return df