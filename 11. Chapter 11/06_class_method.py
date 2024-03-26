class Employee:
    company = "Camel"
    salary = 100
    location = "Kolkata"

    # def changeSalary(self,sal): # change the instance attribute
    #     self.__class__.salary = sal
    # For changing the class attribute
    @classmethod # A Decorator
    def changeSalary(cls,sal):
        cls.salary = sal


e = Employee()
print(e.salary)
e.changeSalary(500)
print(e.salary)
print(Employee.salary)