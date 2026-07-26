import os
def main():
    try:
        # fobj.remove -> Not Applicable
        os.remove("Demo.txt")  

    except FileNotFoundError as fobj:
        print("File is not present in current directly")  

if __name__ =="__main__":
    main()