import pandas as pd

def load_data(file_path="ecommerce_data.csv"):
    """
    Load customer dataset from CSV file.
    """

    try:
        df = pd.read_csv(file_path)
        print("✅ Dataset loaded successfully.")
        return df

    except FileNotFoundError:
        print("❌ Error: File not found.")
        return None

    except Exception as e:
        print("❌ Error:", e)
        return None


def dataset_info(df):
    """
    Display basic dataset information.
    """

    if df is not None:
        print("\n========== First 5 Records ==========")
        print(df.head())

        print("\n========== Dataset Shape ==========")
        print(df.shape)

        print("\n========== Dataset Info ==========")
        print(df.info())

        print("\n========== Missing Values ==========")
        print(df.isnull().sum())

        print("\n========== Statistical Summary ==========")
        print(df.describe())