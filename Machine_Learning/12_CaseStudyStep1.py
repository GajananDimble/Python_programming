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