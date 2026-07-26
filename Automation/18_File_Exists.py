import os

def main():
    Ret=os.path.exists("Demo.txt")

    if(Ret==True):
        print("File is present in current directtory")
    else:
        print("There is no such file")    
    
if __name__ =="__main__":
    main()