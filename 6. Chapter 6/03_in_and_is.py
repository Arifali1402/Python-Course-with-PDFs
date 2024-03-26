# is 

a = None
if(a is None): # "is" points to the object of a and "==" check for value
    print("Yes")
else:
    print("No")

# in
a = [45,56,6]
print(45 in a) # in tells us whether a value is present or not and also helps in for loop
print(435 in a)  # Returns Boolean value