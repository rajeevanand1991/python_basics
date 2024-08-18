score = [10,20,67,45,90]
print(score) #[10, 20, 67, 45, 90]

print(score[0]) #10
#print(score[5]) #IndexError: list index out of range
print(score[4]) #90

#slicing concept
#0,1,2,3,4
#score = [10,20,67,45,90]
#-5,-4,-3,-2,-1
print(score[-1]) #90
print(score[-5]) #10

# new copy the list(shallow copy)
print(score[:]) #[10, 20, 67, 45, 90]

#concatenation
print(score + [1,2,3]) #[10, 20, 67, 45, 90, 1, 2, 3]
print(score + ["A","B","C"]) #[10, 20, 67, 45, 90, 'A', 'B', 'C']

number = [1,2,3,4,5]
number[2] = 90
print(number) #[1, 2, 90, 4, 5]

#Append
number.append(100)
print(number) #[1, 2, 90, 4, 5, 100]
number.append((7**3)) #This is cube of 7 = 7*7*7 = 343
print(number) #[1, 2, 90, 4, 5, 100, 343]

#Update list values
name = ['a','b','c','d','e','f']
print(name) #['a', 'b', 'c', 'd', 'e', 'f']
name[2:5] = ['C','D','E'] #n-1 range, so until 4 will go
print(name) #['a', 'b', 'C', 'D', 'E', 'f']
#Remove list values
name[2:5]=[]
print(name) #['a', 'b', 'f']
#make empty list
name[:] = []
print(name) #[]
name.append([1,2,3])
print(name) #[[1, 2, 3]]

test = [20,30,40,50,60]
print(len(test)) #5 - The length of the list is 5

#nested lists:
a = ['a','b','c']
n = [1,2,3]
x = [a,n]
print(x) #[['a', 'b', 'c'], [1, 2, 3]]
print(x[0]) #['a', 'b', 'c']
print(x[1]) #[1, 2, 3]
print(x[0][1]) #b
print(x[1][2]) #3