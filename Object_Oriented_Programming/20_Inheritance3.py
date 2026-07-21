class Base:
    def __init__(self):
        print("Inside Base Consrutor")

class Derived(Base):
    def __init__(self):
        super().__init__()
        print("Inside derived Constructor")

dobj=Derived()