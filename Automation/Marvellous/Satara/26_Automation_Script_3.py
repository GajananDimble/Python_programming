import sys

def main():
    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("Hello")
        elif(sys.argv[1]=="--u" or "--U"):
            print("Usage") 
        else:       
            DirectoryName =sys.argv[1]
            print("Directory Name is:",DirectoryName)


    else:    
        print("Invalid number of Argument")

        print("Please use --h or --u for more information")

if __name__=="__main__":
    main()