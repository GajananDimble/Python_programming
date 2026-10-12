#----------------------------------
# Deep Learning Pipline
#----------------------------------
# 1.Read The Data from csv
# 2.Data Analusis(EDA)
# 3. Preprocessing
# 4. Train Test Split
# 5. Feature Scaling
# 6. FNN model training
# 7. Model Evaluation
# 8. Gaphical Representation
# 9. Model preserve
# 10. Model loading and preserve
# 11. Test Unseen data
#----------------------------------

border="_"*40
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,confusion_matrix


# Step 1.Read The Data from csv

print(border)
print( "Step 1.Read The Data from csv")
print(border)

data =pd.read_csv("placement_data.csv")

print(data)

# 2.Data Analusis(EDA)
print(border)
print(" 2.Data Analusis(EDA)")
print(border)

print("First five rows:")
print(data.head())

print("Column Name:")
print(data.columns)

print("Shape of Dataset:")
print(data.shape)

print("Statistical Summary:")
print(data.describe())

# Step 3. Preprocessing
print(border)
print(" Step 3. Preprocessing")
print(border)

X = data[['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship']]
Y = data['Placed']

print("Input Features :")
print(X.head())

print("Target :")
print(Y.head())


# Step 4. Train Test Split
print(border)
print("Step 4. Train Test Split")
print(border)

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.30,random_state=42)

print("Traininig input shape :",X_train.shape)
print("Testing input shape :",X_test.shape)
print("Training output shape :",Y_train.shape)
print("Testing Output shape :",Y_test.shape)


# 5. Feature Scaling
print(border)
print(" Step 5. Feature Scaling")
print(border)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled =  scaler.fit_transform(X_test)

print("Scaled Training Data")
print(X_train_scaled[:5])


# 6. FNN model training
print(border)
print("Step 6. FNN model training")
print(border)

model = MLPClassifier(
    hidden_layer_sizes= (8,4),
    activation="relu",
    solver ="adam",
    max_iter= 1000,
    random_state= 42
)

print(model)

print("Train The Model")

model.fit(X_train_scaled,Y_train)
print("Model Training Completed")

# 7. Model Evaluation

print(border)
print("Step 7. Model Evaluation")
print(border)

Y_pred = model.predict(X_test_scaled)

accuracy=accuracy_score(Y_test,Y_pred)
print("Accuracy is :",accuracy)

cm = confusion_matrix(Y_test,Y_pred)
print("Confusion Matrix:",cm)

print("Predict the Probality:")
Y_prob = model.predict_proba(X_test_scaled)
print(Y_prob[:5])


# 9. Model preserve
print(border)
print("Step 9. Model preserve")
print(border)

joblib.dump(model,"Placment_fnn_model.pkl")
joblib.dump(scaler,"Placement_scaler.pkl")

print("Model and Scaler gets dump Successfully")

# 10. Model loading and preserve
print(border)
print("Step 10. Model loading and preserve")
print(border)

loaded_model = joblib.load("Placment_fnn_model.pkl")
loaded_scalar = joblib.load("Placement_scaler.pkl")

print("Model gest loaded Successfully")

# 11. Test Unseen data
print(border)
print("Step 11. Test Unseen data")
print(border)

#---------------------------------
# 11. Test Unseen data
# Aptidtude : 70
# Coding :     75
# Communication  : 80
# Academics :      85
# Internship :     1
#---------------------------------

#new_student = pd.DataFrame([[70,75,80,85,1]])

new_student = pd.DataFrame([[70,75,80,85,1]], columns=['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship'])

new_student_scaled = loaded_scalar.transform(new_student)

new_prediction = loaded_model.predict(new_student_scaled)

new_probablity = loaded_model.predict_proba(new_student_scaled)

print("New students Data : ")
print(new_student)

print("Prediction probablity : ",new_probablity)

if new_prediction[0] == 1:
    print("Prediction : Placed")
else:
    print("Prediction : Not pleaced")