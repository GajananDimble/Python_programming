def Summation(Data):
    Sum=0

    for no in Data:
        Sum=Sum+no
        
    return Sum    

def main():
    Size=0
    Arr=list()

    print("Enter The number of elements:")
    Size=int(input())

    print("Enter The elements:")
    for i in range(Size):
        no=int(input())
        Arr.append(no)

    Ret=Summation(Arr)  
    print("Summation is:",Ret) 

if __name__=="__main__":
    main()