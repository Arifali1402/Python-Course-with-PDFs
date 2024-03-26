num = int(input("Enter the Number: "))
fact = 1
for i in range(1,num+1):
    fact *= i
    
print("Required Factorial is: ")
print(f"{num}!={fact}")
