import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():
    Border="-"*30
    
    # Load The Data
    X=[1,2,3,4,5]
    Y=[3,4,2,4,5]

    print("Values of Independent variable X:",X)
    print("Values of Dependent variable Y:",Y)

    print(Border)
    
    mean_x=np.mean(X)
    mean_y=np.mean(Y) 

    print("Mean_x is :",mean_x)
    print("Mean_y is :",mean_y)

def main():
    MarvellousPredictor()

if __name__=="__main__":
    main()