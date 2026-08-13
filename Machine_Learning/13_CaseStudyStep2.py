import pandas as pd

Border="_"*30
#############################################
# Step 1 : Load The Data Set
#############################################

print(Border)
print("Step 1 : Load The Data Set")
print(Border)

DataPath="iris.csv"

df = pd.read_csv(DataPath)

print("Dataset loaded successfully")

print("Initial Entry From Dataset are:")

print(df.head())

#############################################
# Step 2 : Data Analysis(EDA)
#############################################

print(Border)
print("Step 2 : Data Analysis(EDA)")
print(Border)

print("Shape of DataSet:",df.shape)

print("Column Names:",list(df.columns))

print("Mising values per column:")
print(df.isnull().sum())

print("Class Distribution (Species count):")
print(df["species"].value_counts())

print("Statistical report of DataSet:")
print(df.describe())