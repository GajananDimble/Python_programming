def main():
    try:
        fobj=open("Demo.txt","w")
        print("file gets opened")

        fobj.write("Jay Ganesh...")

        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in current directly")  

if __name__ =="__main__":
    main()