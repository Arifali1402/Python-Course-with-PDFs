from cgi import print_form


num = int(input("Enter the Limit: "))
i = 1
add = 0
while i<=num:
    add += i
    i+=1
print("The Required Sum is "+str(add))
    
