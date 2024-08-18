def login(username, password):
    print(username, password)

#I am calling the function on these ways below:
login("rajeev","test123") #rajeev test123

login(username="rajeevtest",password="test@123") #rajeevtest test@123

# *arg
def getMarks(*arg):
    for x in arg:
        print(x)
#n number of arrays
getMarks(10,23,78,45,80)
#Output:
#10
#23
#78
#45
#80
getMarks("A","A+","B","B-")
#Output:
#A
#A+
#B
#B-

#keyword args:
#represented as **arg

def getStudentMarks(**args):
    for key, value in args.items():
        print("%s == %s" %(key,value))

getStudentMarks(naveen = 10, tom = 20, peter = 30)
#Output:
#naveen == 10
#tom == 20
#peter == 30
getStudentMarks(key = "apple", sellerName = "Xeon")
#output:
#key == apple
#sellerName == Xeon

#Lambda functions: it is an Annonymous function:
#which means a function without any name:

cube = lambda x: x*x*x
print(cube(4)) #64

total = lambda marks: marks+30
print(total(100)) #130