def main():
    try:
        fobj=open("Demo.txt","r")
        print("file gets opened")

        print("File Offset is:",fobj.tell())
        Data=fobj.read(10)
        print(Data)
        print("File Offset is:",fobj.tell())

        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in current directly")  

if __name__ =="__main__":
    main()