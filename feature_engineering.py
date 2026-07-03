import pandas as pd

def feature_engineering(df):
    """
    Create new features for customer segmentation.
    """

    print("\n========== Feature Engineering Started ==========")

    # Average amount spent per purchase
    df["AvgPurchaseValue"] = (
        df["TotalSpent"] / df["PurchaseFrequency"]
    ).round(2)

    # Spending Level
    df["SpendingLevel"] = pd.cut(
        df["SpendingScore"],
        bins=[0, 40, 70, 100],
        labels=["Low", "Medium", "High"]
    )

    # Income Level
    df["IncomeLevel"] = pd.cut(
        df["AnnualIncome"],
        bins=[0, 50000, 75000, 100000],
        labels=["Low", "Medium", "High"]
    )

    # Age Group
    df["AgeGroup"] = pd.cut(
        df["Age"],
        bins=[18, 25, 35, 45, 60],
        labels=["18-25", "26-35", "36-45", "46-60"]
    )

    # Gender Encoding
    df["Gender"] = df["Gender"].map({
        "Male": 0,
        "Female": 1
    })

    print("Feature Engineering Completed Successfully!")

    return df