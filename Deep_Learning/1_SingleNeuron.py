import numpy as np
border="_"*20
print(border)

# Step 1: Define input features ie X
              #[x1 ,x2 ,x3]
input=np.array([2.0,3.0,4.0])
print("X:",input)
print(border)
# Step 2: Define weights ie w
                #[w1 ,w2 ,w3]
weights=np.array([0.5,0.3,0.2])
print("W:",weights)
print(border)

# Step 3: Define Bias ie b
#     b
bias=1.0
print("b:",bias)
print(border)

# Step 4: Calculate weighted sum ie z
# z = x1w1 + x2w2 + x3w3 + b
# z =(2.0*0.5)+(3.0*0.3)+(4.0*0.2)+1.0)

z=np.dot(input,weights)+1.0
print("Z:",z)
print(border)

# Step 5: Activation function (ReLU)

def Relu(x):
    return max(0,x)

# Step 6: Final Output 
Y=Relu(z)
print("Y:",Y)