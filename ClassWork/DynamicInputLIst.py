def main():
    Size=0
    Arr=list()

    print("Enter The number of elements:")
    Size=int(input())

    print("Enter The elements:")
    for i in range(Size):
        no=int(input())
        Arr.append(no)

    print(Arr)    

if __name__=="__main__":
    main()