s1 = "test selenium" #Double quotes are allowed for String [RECOMMENDED]
s2 = 'hello world' #Single quotes are allowed for String

print(s1) #test selenium
print(s2) #hello world

#Array
print(s1[0]) #t
print(s1[12]) #m
#print(s1[13]) #IndexError: string index out of range

#Concatenation
print(s1+" "+s2) #test selenium hello world

#Escape sequence like \n refers to new line
print("hello \n world") #hello
                          #world
#Escape sequence like \t refers to tab space
print("hello \t world") #hello 	 world

#print string 5 times
print("test"*5) #testtesttesttesttest

#Range
print(s1[0:5]) #test

#IN & NOT IN operator
print("test"in s1) #True
print("java" not in s1) #True

#Formatting operator - %s is string and %d is Integer(numeric)
print("my name is %s and my age is %d" %("Tom",25)) #my name is Tom and my age is 25

#print paragraph test within triple quotes
s3 = '''test java
test python
test selenium
and 
this is my python code'''
print(s3) #test java
          #test python
          #test selenium
          #and
          #this is my python code

s4 = """hi this is my python code
and i am learning python
and i am so happy"""
print(s4) #hi this is my python code
          #and i am learning python
          #and i am so happy

#string literals
print('hi i\'m rajeev') #hi i'm rajeev
print("hi my fav programming language is \"python\" and im so happy") #hi my fav programming language is "python" and im so happy

str = "this is my Python code and I love Python"
print(str) #this is my Python code and I love Python
print(str.capitalize()) #This is my python code and i love python => first letter alone get capitalize
print(str.count("Python")) #2 => which means 2 times Python presence in the string
print(str.find("code")) #18 => Code avail on Index position 18th
print(str.find("Rajeev")) #-1
print(len(str)) #40
print(str.lower()) #this is my python code and i love python => Everything converted into lowercase

#lstrip() remove space in left side and rstrip() remove space in right side
str1 = "    hello   "
print(str1.lstrip()) #hello
print(str1.rstrip()) #    hello

#To print highest value of character
print(max(str)) #y

#To print lowest value of character
str2="abz"
print(min(str2)) #a

#Replace string
str3 = "Hello Test Python"
print(str3.replace("Hello","Bye")) #Bye Test Python

#split function
str4 = "java hello python hello javascript"
str5 = str4.split("hello")
print(str5) #['java ', ' python ', ' javascript']
print(str5[0]) #java

print(str4.upper()) #JAVA HELLO PYTHON HELLO JAVASCRIPT

st="Python"
print(st[5]) #n => P->0,y->1,t->2,h->3,o->4,n->5
print(st[-1]) #n => P->-6,y->-5,t->-4,h->-3,o->-2,n->-1
print(st[-6]) #P
print(st[0]) #P

#string comparison using "is"
a = "test rwuiyrewh foeiwuroiwe eoiwrueiwo oiewhrjioewr"
b = "test rwuiyrewh foeiwuroiwe eoiwrueiwo oiewhrjioewr"
print(a is b) #True => It will check only reference value alone
print(a == b) #True => sometimes it goes to false, will check memory area as well