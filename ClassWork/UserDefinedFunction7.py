def Calculation(No1,No2):
    Mult=No1*No2
    Div=No1/No2
    return Mult,Div

def main():
    Value1=int(input("Enter First Number:"))
    Value2=int(input("Enter Second Number:"))

    Ret1,Ret2=Calculation(Value1,Value2)

    print("Multiplication is:",Ret1)
    print("Division is:",Ret2)

if __name__=="__main__":
    main()

#15-16-6-7-8-10-1--2-3-4-10-12-13-15-16