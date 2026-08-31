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

# Step 3: Split Data

#-------------------------------------------------------
# Function Name : SplitData
# Description :   It performs Spliting activity
# Input :         DataFrame
# Output :        4 subsets for training and testing
# Author :        Gajanan Sunil Dimble
# Date :          16/08/2026
#-------------------------------------------------------
def SplitData(df):
    X=df.drop("Survived",axis=1)
    Y=df["Survived"]

    X_train,X_test,Y_train,Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )
    print("DataSet Spliting Completed Succeefully")
    return X_train,X_test,Y_train,Y_test

# Step 4: Train Model

#-------------------------------------------------------
# Function Name : TrainModel
# Description :   It performs model training
# Input :         Trining features and label
# Output :        Trained model
# Author :        Gajanan Sunil Dimble
# Date :          16/08/2026
#-------------------------------------------------------

def Trainmodel(X_train,Y_train):
    model=LogisticRegression(max_iter=1000)

    model=model.fit(X_train,Y_train)
    print("Model Trained successfully")

    return model

# Step 5: Evaluate Model

#-------------------------------------------------------
# Function Name : EvaluateModel
# Description :   It performs model testing
# Input :         model,testing data(features,labels)
# Output :        None
# Author :        Gajanan Sunil Dimble
# Date :          16/08/2026
#-------------------------------------------------------
def EvaluateModel(model,X_test,Y_test):

    Y_pred = model.predict(X_test)

    Accuracy=accuracy_score(Y_test,Y_pred)

    print("Accuracy is :",Accuracy)

    print(confusion_matrix(Y_test,Y_pred))   

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

    # Step 3:
    X_train,X_test,Y_train,Y_test   = SplitData(df) 

    # Step 4:
    model=Trainmodel(X_train,Y_train)

    # Step 5:
    EvaluateModel(model,X_test,Y_test)


if __name__=="__main__":
    main()    