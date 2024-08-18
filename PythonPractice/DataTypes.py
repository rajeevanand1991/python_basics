a=20
print(a+10) # prints 30

#Indentation followed in Python
if (a >= 10) :
    print("Pass") #Prints Pass
else:
    print("Fail")

# Notes
# No need to declare any type of variable. For Example: int, char, string, float, boolean, etc.,
i=10
print(i) #10

i=10+0.1
print(i) #10.1

i= True
print(i) #True

x=50
y=x
print(x) #50
print(y) #50
print(id(x)) #print identity id of x like 140706006695896
print(id(y)) #print identity id of y like 140706006695896

#A-Z a-z 0-9
number_of_months = 12 #Python recommends this varible approach
numberOfMonths = 12 #This also allowed in Python
print(number_of_months, numberOfMonths) #12 12

miles=100.0
name = "Tom"
print(miles, name) #100.0 Tom

a=b=c=1 #multi variable assignment allowed for single value allowed in Python
print(a, b, c) #1 1 1

a,b,c = 3,4,"Rajeev" #1to1 assignment allowed in Python
print(a, b, c) #3 4 Rajeev

min_bal=100
print(min_bal) #100

i="test"
print(i) #test

s1 = "Hello World PYTHON"
print(s1[0]) #prints only H
print(s1[2:6]) #prints llo
print(s1[2:]) #prints llo World PYTHON
print(s1*3) #prints Hello World PYTHONHello World PYTHONHello World PYTHON
print(s1+" "+"Programming") #prints Hello World PYTHON Programming