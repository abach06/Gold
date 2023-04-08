import random

var = []

print(type(var))

var2 = [251, 386, 493]

print(var2)

#var2.insert(3, 649)

#print(var2)
    

var3 = [251, 386, 493, "009"]

var3.append(649) #inplace function
var3 = var3 + [721] # Not in place function

#var3.insert(4, 649)





#print(dir(var3))

var3.reverse()

print(var3)

numbers = [1,2,3,4,5]
print(numbers)

r = range(0, 20)

print(r)

print(list(r))


for number in numbers:
    print(number*2)
    
for i in range(0, 10):
    print(i)

print(var3)
print(var3[1])

print(len(var3))

for i in range(len(var3)):
    print(var3[i])
    

"""
Your module description
"""
