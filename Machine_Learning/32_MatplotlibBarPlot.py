import matplotlib.pyplot as plt

def main():
    Language=["C","C++","Java","Python"]
    students=[30,40,35,55]

    plt.bar(
        Language,                     # Values of X axis
        students,                     # Values of Y axis
        width=0.6,                    # Width of bar
        edgecolor="black",            # border color of bars
        linewidth=1,                  # width of bar border
        alpha=0.8,                    # transperence 0.0 to 1.0
        label="Students"              # legend text
    )

    plt.title("Marvellous Bar Plot")
    plt.xlabel("Language")
    plt.ylabel("students")


    plt.legend()
    plt.show()

if __name__=="__main__":
    main()