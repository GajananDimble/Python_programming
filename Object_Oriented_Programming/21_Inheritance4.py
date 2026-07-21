class Base:
    def __init__(self):
        print("Inside Base Consrutor")

    def fun(self):
        print("Inside Base Fun")    

class Derived(Base):
    def __init__(self):
        super().__init__()
        print("Inside derived Constructor")

dobj=Derived()

dobj.fun()