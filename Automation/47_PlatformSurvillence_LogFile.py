import psutil
import sys
import os

def PlatformSurvillence(FolderName):
    Border="_"*50

    Ret=False
    Ret=os.path.exists(FolderName)

    if(Ret==True):
        Ret=os.path.isdir(FolderName)
        if(Ret==False):
            print("Unable To Proceed As Directory Name is existing but its not a directory")
            return
    else:
        os.mkdir(FolderName)
        print("Directory For The Log File Gets Created succesfully")

def main():
    Border="_"*60
    print(Border)
    print("-----Marvellous Platfrom Survillence Sysytem------")
    print(Border)

    # --h and --u Handling
    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This Automation Script is use to perform")
            print("1:It fetch the information of running processes")
            print("2:It fetch information about the primary storage as RAM")
            print("3:It fetch information about the secondry storage as HDD")
            print("4:It fetch the information about the Microproceesor")
            print("5:It gets auto scheduled periodically")
            print("6:It maintancen all records into log file")
            print("7:It sends the log files through mail perodically")

        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Use the automation Script as:")
            print(f"Python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval:Time in minutes for periodic execution")
            print("Folder_Name:Name of folder For the log Creation")

        else:
            print("Unable to proceed as argument are not matching")
            print("Please use --h or --u flag for getting more details")
    
    # Acual Project Code
    elif(len(sys.argv)==3):
        PlatformSurvillence(sys.argv[2])


    else:
        print("Invalid Number of argument")
        print("Unable to proceed as argument are not matching")
        print("Please use --h or --u flag for getting more details")


    print(Border)
    print("--Thank You For Using Marvellous Automation System--")
    print(Border)


if __name__=="__main__":
    main()