#set
a = {2,3,4,5,8,9,7,6,5,1}
print(a)

#adding a number in the set
a.add(10)
print(a)
b = {3,4,5,6,2,7,8,9,1,11}

#printing the a and b set together
print(a.union(b))

#printing the same numbers between a and b
print(a.intersection(b))

#printing the different numbers between a and b
print(a.symmetric_difference(b))