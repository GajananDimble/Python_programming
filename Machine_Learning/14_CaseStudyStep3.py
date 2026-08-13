import pandas as pd

Broder="_"*30
#############################################
# Step 1 : Load The Data Set
#############################################

print(Broder)
print("Step 1 : Load The Data Set")
print(Broder)

DataPath="iris.csv"

df = pd.read_csv(DataPath)

print("Dataset loaded successfully")

print("Initial Entry From Dataset are:")

print(df.head())

#############################################
# Step 2 : Data Analysis(EDA)
#############################################

print(Broder)
print("Step 2 : Data Analysis(EDA)")
print(Broder)

print("Shape of DataSet:",df.shape)

print("Column Names:",list(df.columns))

print("Mising values per column:")
print(df.isnull().sum())

print("Class Distribution (Species count):")
print(df["species"].value_counts())

print("Statistical report of DataSet:")
print(df.describe())

#############################################
# Step 3 : Deside Independent & Dependent variables
#############################################

print(Broder)
print("Step 3 : Deside Independent & Dependent variables")
print(Broder)

# X: Independent Variables/Features
# Y: Dependent Varoables/Labels

feature_cols=[
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)",
    ]

X=df[feature_cols]
Y=df["species"]

print("X Shape:",X.shape)
print("Y Shape:",Y.shape)

