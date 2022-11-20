class Employee:
    company = "Google" # Specific to each class
    salary = 100

harry = Employee() # Object Instantiation
arif = Employee()

# Creating instance attribute for both the objects

# Instance attribute take preference over the class attribute
harry.salary = 300 # Instance attribute
# arif.salary = 100 
print(harry.salary)
print(arif.salary)
# print(arif.address) # Throws an error as 'Employee' object has no attribute 'address' as address is not present in the instance/class