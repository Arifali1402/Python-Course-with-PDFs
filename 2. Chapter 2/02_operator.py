from cgi import print_form
from tkinter import E
a = 3
b = 4
# Arithmetic operators
print("the value is a+b is", a+b)
print("the value is a-b is", a-b)
print("the value is a*b is", a*b)
print("the value is a/b is", a/b) #(int/int) = float
# print("the value is b/a is", b/a)

# Assignment Operators
a = 34
a +=12
a *=13
a /=1 # Division always give you a floating point value as an output
print(a)
# Comparison Operator

a = (4>7)
b = (4>=7)
c = (4<7)
d = (4<=7)
e = (7 == 7)
print(a) # Gives a Boolean Return
print(b) # Gives a Boolean Return
print(c) # Gives a Boolean Return
print(d) # Gives a Boolean Return
print(e) # Gives a Boolean Return

#Logical Operators

bool1 = True
bool2 = False
print("The value of bool1 and bool2 is", (bool1 and bool2))
print("The value of bool1 or bool2 is", (bool1 or bool2))
print("The value of not bool1 is", (not bool1)) # Not only takes 1 variable
print("The value of not bool2 is", (not bool2))