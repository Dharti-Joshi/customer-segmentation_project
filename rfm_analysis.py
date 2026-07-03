import pandas as pd

def rfm_analysis(df):
    """
    Perform RFM Analysis.

    Note:
    This dataset does not contain PurchaseDate,
    so Recency cannot be calculated.
    """

    print("\n========== RFM ANALYSIS ==========")

    # Create RFM DataFrame
    rfm_df = pd.DataFrame()

    rfm_df["CustomerID"] = df["CustomerID"]

    # Recency (Not Available)
    rfm_df["Recency"] = 0

    # Frequency
    rfm_df["Frequency"] = df["PurchaseFrequency"]

    # Monetary
    rfm_df["Monetary"] = df["TotalSpent"]

    # Frequency Score
    rfm_df["F_Score"] = pd.qcut(
        rfm_df["Frequency"],
        3,
        labels=[1, 2, 3]
    )

    # Monetary Score
    rfm_df["M_Score"] = pd.qcut(
        rfm_df["Monetary"],
        3,
        labels=[1, 2, 3]
    )

    # Overall FM Score
    rfm_df["FM_Score"] = (
        rfm_df["F_Score"].astype(str) +
        rfm_df["M_Score"].astype(str)
    )

    # Customer Segment
    def segment(score):
        if score == "33":
            return "High Value"

        elif score in ["32", "23"]:
            return "Loyal"

        elif score in ["22", "21", "12"]:
            return "Regular"

        else:
            return "Low Value"

    rfm_df["CustomerSegment"] = rfm_df["FM_Score"].apply(segment)

    print(rfm_df.head())

    return rfm_df