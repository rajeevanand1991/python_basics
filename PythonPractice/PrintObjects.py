# string representation of class object:
# Object printing concept: In Java, we will use toString() method
class Test:

    def __init__(self,x,y): #constructor declared
        self.x = x
        self.y = y
        #if no declared of below repr and str methods, it will give memory allocation reference address simply
        #<__main__.Test object at 0x000002BACB5532F0>

    def __repr__(self): #If no delcared of below str method, this method will called by default
        return "x:%s y:%s" % (self.x, self.y) #x:10 y:20

    def __str__(self): #This str method called by default, while calling the class object
        return "value of x is %s and y is %s" % (self.x, self.y)

#Test code:
t = Test(10,20)
print(t) #value of x is 10 and y is 20