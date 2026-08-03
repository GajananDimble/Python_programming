import psutil
import sys
import os
import time
import schedule

def PlatformSurvillence(FolderName):
    Border = "_" * 50

    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to proceed as folder name is existing but its not a directory")
            return 
    else:
        os.mkdir(FolderName)
        print("Directory for the log file gets created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName, "Marvellous_%s.log" %timestamp)

    fobj = open(FileName, "w")

    print(f"Log file gets successfully created with name {FileName}")

    fobj.write(Border + "\n")
    fobj.write("_____Marvellous Platform Survillence System_____\n")
    fobj.write("Log file gets created at :" + timestamp + "\n")
    fobj.write(Border + "\n")

    fobj.write("----------Sysytem report----------\n")

    # CPU INformation
    fobj.write("Number of active CPU usage : %s\n" %psutil.cpu_count())
    fobj.write("CPU usage : %s %%\n" %psutil.cpu_percent())
    fobj.write(Border + "\n")

    # RAM Information
    memory = psutil.virtual_memory()

    fobj.write("RAM usage : %s %%\n" %memory.percent)
    fobj.write("Total RAM available : %s\n" %memory.total)
    fobj.write(Border + "\n")

    fobj.write(Border + "\n")
    fobj.write("----------End of log file----------\n")
    fobj.write(Border + "\n")

    fobj.close()

def main():
    Border = "_" * 50
    print(Border)
    print("_____Marvellous Platform Survillence System_____")
    print(Border)

    # --h & --u handling
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to perform")
            print("1 : It fetch the information of running processess")
            print("2 : It fetches information about the primary storage as RAM")
            print("3 : It fetches information about the secondary storage as HDD")
            print("4 : It fetch the information about the microprocessure")
            print("5 : It gets auto schedued periodically")
            print("6 : It maintains all records into the log files")
            print("7 : It sends the log files through email periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as :")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval : Time in minutes for peroidic execution")
            print("Folder_Name : Name of folder for thr log creation")
            
        else:
            print("unable to proceed as there is no matching argument")
            print("Please use --h or --u flag for geting more details")

    # Actual project code
    elif(len(sys.argv) == 3):

        # print("CPU uasge :", psutil.cpu_percent())
        print("Schedular started succesfully")
        print("Press ctrl + c to abort the automation script")

        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvillence, sys.argv[2])

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid Number of arguments")
        print("Unable to proceed as arguments are not matching")
        print("Please use --h or --u flag for geting more details")

    print(Border)
    print("----Thank you for using our automattion system----")
    print(Border)

if __name__ == "__main__":
    main()