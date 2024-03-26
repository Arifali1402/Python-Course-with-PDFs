# greeting = "Good Morning, "
# name  = "Arif"
# print(type(name))
# Concatenating two Strings
# c = greeting+name
# print(c)
name  = "Arif Ali"
print(name[3])
# name[3] = "d" -->'str' object does not support item assignment
print(name[0:6]) #--> prints from 0 to 5(not from 0 to 6)
print(name[2:6]) #--> prints from 2 to 5(not from 2 to 6)
print(name[:3]) #--> Same as 0 to [0:3]
print(name[3:]) #-->same as [3:length]
c = name[-4:-1] 
print(c) #--> same as name[4:7]
print(name[4:7]) #-->same as [3:length]
#Over writing name
name  = "ArifAliIsAGoodBoy"

d = name[0::3] #skip value of 3
print(d)
