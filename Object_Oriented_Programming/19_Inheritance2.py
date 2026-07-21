class Base:
    def __init__(self):
        print("Inside Base Consrutor")

class Derived(Base):
    def __init__(self):
        print("Inside derived Constructor")

bobj=Base()