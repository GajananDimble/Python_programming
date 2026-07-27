import sys
import os
import time

def DirectoryScanner(DirectoryPath):

    timestamp=time.ctime()
    LogFileName="Marvellous%s.log"%(timestamp)
    LogFileName=LogFileName.replace(" ","_")
    LogFileName=LogFileName.replace(":","_")
    

    print("File File Gets Created With :",LogFileName)

    fobj=open(LogFileName,"w")
    
    fobj.write("Marvellous Automation Script \n")

    fobj.write("File from the directory are:\n")

    for FolderName,SubFloder,FileName in os.walk(DirectoryPath):
        for Fname in FileName:
            fobj.write(Fname+"\n")

    fobj.close()        

def main():
    Border="-"*40
    
    print(Border)
    print("Marvellous Automation Script")
    print(Border)

    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This Automation Script is used to travel the directory")
            print("For Better usage plese check --u flag")

        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Please execute the script as")
            print("Python FileName.py Directory Name") 
            print("Directory Name Should Be absolute path")
        else:       
            DirectoryScanner(sys.argv[1])

    else:    
        print("Invalid number of Argument")

        print("Please use --h or --u for more information")

    print(Border)
    print("Thank You for using marvellous Automation")
    print(Border)        

if __name__=="__main__":
    main()