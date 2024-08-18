class Person(object):

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False


class Employee(Person):

    # Method Overriding is same method name taken from the parent class
    def isEmployee(self):
        return True

#Test Person
emp = Person("Rajeev")
print(emp.name) #Rajeev
print(emp.getName(), emp.isEmployee()) #Rajeev False

emp1 = Employee("Tom")
print(emp1.name) #Tom
print(emp1.getName()) #Tom
print(emp1.isEmployee()) #True