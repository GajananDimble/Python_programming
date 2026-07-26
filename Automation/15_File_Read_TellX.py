def main():
    try:
        fobj=open("Demo.txt","r")
        print("file gets opened")

        print("File Offset is:",fobj.tell())    # 0
        Data=fobj.read(10)
        print(Data)
        print("File Offset is:",fobj.tell())    # 10

        Data=fobj.read(10)                      # 10
        print(Data)
        print("File Offset is:",fobj.tell())    # 20

        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in current directly")  

if __name__ =="__main__":
    main()