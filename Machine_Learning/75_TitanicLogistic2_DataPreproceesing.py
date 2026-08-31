import pandas as pd
import numpy as np
import joblib 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

# Step 1: Load the Data
#-------------------------------------------------------
# Function Name : Load Data
# Description :   Load the data from csv
# Input :         Name of the CSV file
# Output :        Data Frame
# Author :        Gajanan Sunil Dimble
# Date :          16/08/2026
#-------------------------------------------------------
def LoadData(filename):
    df=pd.read_csv(filename)

    print("Dataset loaded successfully")

    print(df.head())
    return df

# Step 2: Data Preprocessing

#-------------------------------------------------------
# Function Name : PreProcess Data
# Description :   It performs Data Anlyatics
# Input :         DataFrame
# Output :        Updated DataFrame
# Author :        Gajanan Sunil Dimble
# Date :          16/08/2026
#-------------------------------------------------------
def PreProcess(df):
    df = df.drop([
        "Passengerid",
        "zero",
        "name"
    ],
    errors="ignore")
    # Handle missing values

    df ["Age"] = df["Age"].fillna(df["Age"].median())
    df ["Fare"] = df["Fare"].fillna(df["Fare"].median())

    df ["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    # Convert categorical to numeric data
    df=pd.get_dummies(
        df,
        columns=["Embarked"],
        drop_first=True,
        dtype=int
    )

    print(df.head())
    print("Data Preprocessing completed")

    return df

#-------------------------------------------------------
# Function Name : main
# Description :   Entry point function
# Input :         None
# Output :        None
# Author :        Gajanan Sunil Dimble
# Date :          16/08/2026
#-------------------------------------------------------
def main():
    # Step 1
    df =LoadData("MarvellousTitanicDataset.csv")  

    # Step 2:
    df = PreProcess(df) 

if __name__=="__main__":
    main()    