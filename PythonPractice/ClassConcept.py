class Car:

    #class variables
    wheels = 4

    #Constructor of this class:
    def __init__(self):
        print("Default constructor")

    def __init__(self, color):
        print("Car class constructor")
        self.color = color

    def test(self):
        print("test method")

    #if any var is declared inside the method or constructor: instance variable
    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

#How to create an Object of this class:
c1 = Car("Red")
print(c1.wheels)
print(Car.wheels) #we can directly call with class variables, but in Java it wont allowed due to static variable alone can include it in main method

c1.test()
c1.setPrice(1000)
print(c1.getPrice())

c2 = Car("Black")
c1.setPrice(3000)
print(c1.getPrice())

#one class for example:
class Test:
    a = 10

#Blank class:
class Pop:
    pass

p1 = Pop()