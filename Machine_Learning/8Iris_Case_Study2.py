from sklearn.datasets import load_iris

def main():
    print("_"*30)
    print("Iris Classification Case Study")
    print("_"*30)

    Dataset=load_iris()

    #MetaData of Dataset
    print("Independent Variales Are:")
    print(Dataset.feature_names)

    print("Dependent Variales Are:")
    print(Dataset.target_names)    

if __name__=="__main__":
    main()