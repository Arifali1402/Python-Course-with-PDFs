#Creating a Tuple using ()

t = (1,2,4,3)
#Printing the elements of the tuple 
print(t)
#Printing the element of tuples using t[]
print(t[3])

#We cannot change the values of a tuple's element
#t[2] = 67 --> major difference between list and tuple

#Empty Tuple
t1 = ()
print(t1)

#Tuple with only one element needs a comma
# t2 = (1) --> Wrong way to declare a tuple with one element
t2 = (1,)
print(t2)