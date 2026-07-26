import os

def main():
    for FolderName,SubFolder,FileName in os.walk("Marvellous"):
        print("FolderName:",FolderName)

        for subf in SubFolder:
            print("Subfolder Name:",subf)

        for fname in FileName:
            print("FileName:",fname)    

if __name__=="__main__":
    main()    