def main():
    try:
        open("Demo.txt","w")
        print("file gets opened")

    except FileNotFoundError as fobj:
        print("File is not present in current directly")  

if __name__ =="__main__":
    main()