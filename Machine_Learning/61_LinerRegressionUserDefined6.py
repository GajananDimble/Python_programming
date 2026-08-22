import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():
    Border="-"*50
    
    # Load The Data
    X=[1,2,3,4,5]
    Y=[3,4,2,4,5]

    print(Border)

    print("Values of Independent variable X:",X)
    print("Values of Dependent variable Y:",Y)

    print(Border)
    
    sum_x=0
    sum_y=0

    for i in range(len(X)):
        sum_x=sum_x+X[i]
        sum_y=sum_y+Y[i]

    mean_x=sum_x/len(X)
    mean_y=sum_y/len(Y)    

    print("Mean_x is :",mean_x)
    print("Mean_y is :",mean_y)

    print(Border)

    n=len(X) #  5

    numerator=0
    denomerator=0

    # Calculate slope i.e m

    for i in range(n):
        numerator=numerator +((X[i]-mean_x)*(Y[i]-mean_y))

        denomerator=denomerator+((X[i]-mean_x)**2)

    m=numerator/denomerator
    print("Slope of line ie m:",m)

    print(Border)   

    # y = mx+c
    # c = y-mx
    # c = ymean - m * xmean

    c = mean_y-m* mean_x

    print("Y Intercept ie C:",c)
    print(Border)

    x = np.linspace(1,6,n)
    y =c + m * x

    plt.plot(x,y,color='g',label="Regression Line")
    plt.scatter(X,Y,color='r',label="Scatter Plot")

    plt.xlabel("X: Independent Variables")
    plt.ylabel("Y: Dependent Variables") 

    plt.grid(True)      

    plt.legend()
    plt.show()

     
def main():
    MarvellousPredictor()

if __name__=="__main__":
    main()