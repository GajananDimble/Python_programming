# 6: 1*2*3*4*5*6

def Factorial(no):
    Fact=1

    for i in range(1,no+1):
        Fact=Fact*i

    return Fact    
def main():
    value=int(input("Enter Number:"))

    Ret=Factorial(value)

    print(f"Factorial of {value} is {Ret}")

if __name__=="__main__":
    main()