class Employee:
    company = "Camel"
    salary = 100
    location = "Kolkata"

    # def changeSalary(self,sal): # add an instance attribute
    #     self.__class__.salary = sal
    @classmethod # A Decorator
    def changeSalary(cls,sal):
        cls.salary = sal
        
        

e = Employee()
print(e.salary)
e.changeSalary(500)
print(e.salary)
print(Employee.salary)
