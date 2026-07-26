import os

def main():
    for FolderNAme,SubFolder,FileName in os.walk("Marvellous"):
        print(FolderNAme)

if __name__=="__main__":
    main()    