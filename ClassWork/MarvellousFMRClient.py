from MarvellousLibrary import filterX,mapx,reduceX

from functools import reduce

CheckEven=lambda No:(No % 2 == 0)
Increment=lambda No:No+1
Addition=lambda No1,No2:No1+No2


def main():
    Data=[13,12,8,10,11,20]

    print("Inupt Data is:",Data)

    FData=list(filterX(CheckEven,Data))
    print("Data After Filter:",FData)

    MData=list(mapx(Increment,FData))
    print("Data after MData:",MData)

    RData=reduceX(Addition,MData)
    print("Data After Reduce :",RData)
    

    
if __name__=="__main__":
    main()    