import sys

def main():
    print("----------------------------------------------------------")
    print("-----------------Automation Script------------------------")
    print("----------------------------------------------------------")

    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This Automation Script is used to travel the directory")
            print("FFor Better usage plese check --u flag")

        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Please execute the script as")
            print("Python FileName.py Directory Name") 
            print("Directory Name Should Be absolute path")
        else:       
            DirectoryName =sys.argv[1]
            print("Directory Name is:",DirectoryName)


    else:    
        print("Invalid number of Argument")

        print("Please use --h or --u for more information")

    print("----------------------------------------------------------")
    print("-----------------Tahnk Yoy -------------------------------")
    print("----------------------------------------------------------")        

if __name__=="__main__":
    main()