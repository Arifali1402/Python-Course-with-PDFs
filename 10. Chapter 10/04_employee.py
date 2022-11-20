class Employee:
    company = "Google" # Specific to each class
    salary = 100
harry = Employee() # Object Instantiation
arif = Employee()
harry.salary = 300 # Instance attribute
arif.salary = 100
# Instance attribute take preference over the class attribute
print(harry.salary)
print(arif.salary)
print(harry.company)
print(arif.company)
Employee.company = "YouTube" # Class Attribute can be changed
print(harry.company)
print(arif.company)
