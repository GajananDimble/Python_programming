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

if __name__=="__main__":
    main()