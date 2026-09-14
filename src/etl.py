import pandas as pd
import os


def extract_data():
    print("EXTRACT: Reading data sources...")

    sales = pd.read_csv("data/sales.csv")
    customers = pd.read_csv("data/customers.csv")

    print("Sales data loaded successfully.")
    print("Customer data loaded successfully.")

    return sales, customers


def transform_data(sales, customers):
    print("\nTRANSFORM: Processing data...")

    df = pd.merge(sales, customers, on="customer_id", how="inner")

    df["total_amount"] = df["quantity"] * df["price"]

    df = df.dropna()

    df["customer_name"] = df["customer_name"].str.upper()

    print("Data transformation completed.")

    return df


def load_data(df):
    print("\nLOAD: Saving processed data...")

    os.makedirs("output", exist_ok=True)

    df.to_csv("output/processed_sales.csv", index=False)

    print("Processed data saved successfully.")
    print("Output file: output/processed_sales.csv")


def main():
    print("=" * 50)
    print("MULTI-SOURCE ETL PIPELINE STARTED")
    print("=" * 50)

    sales, customers = extract_data()

    df = transform_data(sales, customers)

    load_data(df)

    print("\n" + "=" * 50)
    print("ETL PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 50)


if __name__ == "__main__":
    main()