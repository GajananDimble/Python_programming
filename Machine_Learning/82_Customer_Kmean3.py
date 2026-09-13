import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def main():
    # Step 1: Load Data

    df=pd.read_csv("Mall_Customers.csv")

    print("Dataset Loaded with values:")

    print(df.head())

    print("Missing Values")
    print(df.isnull().sum())

   # Step 2: Feature Selection

    X = df[["AnnualIncome","SpendingScore"]]

    print(X.head())

    # step 3: scale the data

    scaler=StandardScaler()

    X_scaled=scaler.fit_transform(X)

    print("Scaled Data:")
    print(X_scaled[:5])


if __name__=="__main__":
    main()