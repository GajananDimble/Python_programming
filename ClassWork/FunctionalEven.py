CheckEven=lambda No:(No%2==0)
    
def main():
    Value=int(input("Enter number:"))

    Ret=CheckEven(Value)             #Re=(value%2==0)

    if(Ret==True):
        print("Its Even Number")
    else:
        print("Its Odd Number")    
if __name__=="__main__":
    main()