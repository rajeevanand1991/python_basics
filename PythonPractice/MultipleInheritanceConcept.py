class Base1(object):
    def __init__(self):
        self.str1 = "Rajeev"
        print("Base1")

class Base2(object):
    def __init__(self):
        self.str2 = "Tom"
        print("Base2")

class Child(Base1, Base2): #Multiple Inhertance allowed in Python not in Java
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)

        print("Child")

    def printStrings(self):
        print(self.str1, self.str2)

ob = Child() #This call constructor while object creation:
#output:
#Base1
#Base2
#Child

ob.printStrings() #Rajeev Tom