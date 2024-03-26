n1 = int(input("Enter Number 1: "))
n2 = int(input("Enter Number 2: "))
n3 = int(input("Enter Number 3: "))
n4 = int(input("Enter Number 4: "))

# if(n1>n2 and n1>n3 and n1>n4):
#     print(str(n1),"is the greatest")
# elif(n2>n3 and n2>n4):
#     print(str(n2),"is the greatest")    
# elif(n3>n4):
#     print(str(n3),"is the greatest")
    
# else:
#     print(str(n4),"is the greatest")
    

# Alternate Method

if(n1>n4):
    # pass ---> will be filled later
    f1 = n1
else:
    f1 = n4
if(n2>n3):
    f2 = n2
else:
    f2 = n3

if(f1>f2):
    print(f1,"is the Greatest")
else:
    print(f2,"is the Greatest")
