#while loop:
count = 0
while (count<3):
    print("Hello world")
    print(count)
    count = count + 1
#output:
#Hello world
#0
#Hello world
#1
#Hello world
#2

print("------------------")
num = 0
while (num < 3):
    print("Hello Python")
    num = num + 1
else:                   # This else: block not present in Java on while loop
    print("Bye Python")
#output:
#Hello Python
#Hello Python
#Hello Python
#Bye Python

print("------------------")
#for loop:
name = ["java", "python", "dot net", "c sharp"]
for i in name:
    print(i)
#output:
#java
#python
#dot net
#c sharp

print("------------------")
str = "I love python"
for i in str: #we can use it for Iteration as well
    print(i)
#output
#I

#l
#o
#v
#e

#p
#y
#t
#h
#o
#n
print("------------------")
list = ["Naveen", "Automation", "Labs"]
for index in range(len(list)):
    print(list[index])
#output
#Naveen
#Automation
#Labs
print("------------------")

#for loop with else:
Countrylist = ["India", "USA", "UK", "Germany"]
for index in range(len(Countrylist)):
    print(Countrylist[index])
else:
    print("Countrylist is over")
#output
#India
#USA
#UK
#Germany
#Countrylist is over
print("------------------")

Citylist = ["Bangalore", "NY", "LA", "Berlin"]
for index in range(2):
    print(Citylist[index])
else:
    print("Citylist is over")
#output
#Bangalore
#NY
#Citylist is over

print("------------------")
#nested for loop:
for i in range(1,5):
    for j in range(i):
        print(i, end='')
    print()
#output
#1
#22
#333
#4444