name = "Alexander"
for i in name:
    print(i)
    if(i=="x"):
        break   # it will break the loop if condition satisfied
#output:
#A
#l
#e
#x
print("------------")
name = "Alexander"
for i in name:
    print(i)
    if(i=="x"):
        continue # it will continue the loop eventhough if condition satisfied
#output:
#A
#l
#e
#x
#a
#n
#d
#e
#r

str = ["python", "java", "C sharp", "Dot Net"]
for l in range(len(str)):
    print (str[l])
    if(str[l]=="java"):
        print("hey I found Java!!!")
        break
#output:
#python
#java
#hey I found Java!!!
print("------------")
str = ["python", "java", "C sharp", "Dot Net"]
for l in range(len(str)):
    print (str[l])
    if(str[l]=="java"):
        print("hey I found Java!!!")
        continue
#output:
#python
#java
#hey I found Java!!!
#C sharp
#Dot Net
print("------------")
lang = ["Hindi", "English", "Spanish", "German", "Chinese"]
flag = False
for index in range(len(lang)):
    print (lang[index])
    if(lang[index]=="Spanish"):
        print ("Spanish is the 2nd popular language in the world")
        flag = True
        break
if(flag):
        print("I want to learn Spanish")
#output:
#Hindi
#English
#Spanish
#Spanish is the 2nd popular language in the world
#I want to learn Spanish