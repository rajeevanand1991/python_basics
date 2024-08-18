class Employee:

    #hidden data member or private member of Employee class
    __salary = 1000 #In Java, we will use private keyword

e1 = Employee() #e1 object created
#print(e1.__salary) -- This is not the right way of accessing hidden private variable

#Access private hidden variable by using tricky syntax:
print(e1._Employee__salary) #1000