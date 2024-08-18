m = int(input("please enter the value of m")) #To print runtime value from the user (same like Scanner class in Java)
print(m+100) # please enter the value of x20
             # 120

x = int(input("please enter the value of x"))

if(x<0):
    print("x is negative number")
elif(x>0):
    print("x is positive number")
elif(x==0):
    print("x is equal to zero") # please enter the value of x5
                                # x is positive number
                                # PASS
else:
    print("not defined")

if True:
    print("PASS") #PASS
else: #dead code (it will not come this block, because if block by default set it as True)
    print("FAIL")

if (10>5):
    print("Hii") #Hii

#WAP (Write A Program) to find out the highest number
a = 100
b = 200
c = 300
if (a>b) and (a>c):
    print("a is the highest number")
elif (b>c):
    print("b is the highest number")
else:
    print("c is the highest number") #c is the highest number

total = int(input("enter the total value:"))
if(total<100):
    total = total + 20
elif(total>=100 and total<=500):
    total = total + 50
else:
    total = total + 100
print(total) # enter the total value:100 #no concat
             # 150
print("total = "+str(total)) #total = 150 it is using str() method
print(f'{"Total value = "}{total}') # using f strings formula