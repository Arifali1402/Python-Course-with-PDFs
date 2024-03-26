# Creating an Empty Set
x = set()
print(type(x))
# Adding elements to the set
x.add(4)
x.add(5)
x.add(5) # wont add same value multiple times
# x.add([3,5,7]) # Cannot add list in a set because list is not hashable
x.add((3,3,5,7)) # Can add tuple in a set as it is hashable

# x.add({4:5}) # Cannot add Dictionary in a set
print(x)
print(len(x)) # Prints the length of the set

x.remove(4) # Removes 4 from the set
# x.remove(9) # Throws an error while trying to remove 9(Which is not present in the set)  
print(x) 
print(x.pop())
print(x.pop())

#...............................................................

p = {4,5,6,7,4,3,6}
q = {1,2,3,4,54,56,6,8,8,5}
print(p.intersection(q))
print(p.union(q))