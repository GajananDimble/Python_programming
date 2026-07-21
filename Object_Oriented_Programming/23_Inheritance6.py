# multiple inheritance
class Base1:
    def fun(self):
        print("Inside Base1 Fun")    

class Base2:
    def gun(self):
        print("Inside Base2 gun")    

class Derived(Base1,Base2):
    def sun(self):
        print("Inside Derived Sun")

dobj=Derived()

dobj.fun()
dobj.gun()
dobj.sun()