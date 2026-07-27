#####################################################
# 
# Importing required Libraries
#  
#####################################################
import sys
import os
import time
import schedule

#####################################################
# Function Name:   DirectoryScanner
# Input :          Name Of Directory
# Description :    Delets all Empty files Periodically
# Date:            19/07/2026
# Author:          Gajanan Sunil Dimble
#####################################################

def DirectoryScanner(DirectoryPath):

    Border="_"*40

    timestamp=time.ctime()
    LogFileName="Marvellous%s.log"%(timestamp)
    LogFileName=LogFileName.replace(" ","_")
    LogFileName=LogFileName.replace(":","_")

    Ret=False
    Ret=os.path.exists(DirectoryPath)

    if(Ret==False):
        print("Marvellous Automation Error : There is no such directory with name",DirectoryPath)
        return 
    
    Ret=os.path.isdir(DirectoryPath)
    
    if(Ret==False):
        print("Marvellous Automation Error: It is not a Directory with name:",DirectoryPath)
        return
    
    print("File File Gets Created With :",LogFileName)

    fobj=open(LogFileName,"w")

    fobj.write(Border+"\n")
    fobj.write("Marvellous Automation Script \n")
    fobj.write(Border+"\n\n")

    fobj.write("File from the directory are:\n\n")
    fobj.write(Border+"\n")

    TotalFiles=0
    EmptyFiles=0  

    for FolderName,SubFloder,FileName in os.walk(DirectoryPath):
        for Fname in FileName:
            TotalFiles=TotalFiles+1


            Fname=os.path.join(FolderName,Fname)
            fobj.write(Fname+":"+str(os.path.getsize(Fname))+"bytes\n")

            if(os.path.getsize(Fname)==0):
                EmptyFiles=EmptyFiles+1
                os.remove(Fname)

    fobj.write(Border+"\n")
    fobj.write("Total Files Scanned:"+str(TotalFiles)+"\n")
    fobj.write("Total Empty files Found And Deleted:"+str(EmptyFiles)+"\n")


    fobj.write(Border+"\n")
    fobj.write("Log File Gets Created at:"+timestamp)
    fobj.write("\n"+Border+"\n")

    fobj.close()        
#####################################################
# Function Name:   Main
# Input :          Command Line Arguments
# Description :    It contros the Script
# Date:            19/07/2026
# Author:          Gajanan Sunil Dimble
#####################################################

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
            schedule.every(1).minute.do(DirectoryScanner,sys.argv[1])
            DirectoryScanner(sys.argv[1])
            while True:
                schedule.run_pending()
                time.sleep(1)         

    else:    
        print("Invalid number of Argument")

        print("Please use --h or --u for more information")

    print(Border)
    print("Thank You for using marvellous Automation")
    print(Border)        
#####################################################
# 
# Starter of the automation script 
# 
#####################################################
if __name__=="__main__":
    main()