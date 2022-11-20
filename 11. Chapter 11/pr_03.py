class Employee:
    salary = 50000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,val): # val = salary after increment
        self.increment = val/self.salary

e = Employee()
print(e.salary)
print(e.salaryAfterIncrement)
print(e.increment)
e.salaryAfterIncrement = 51000 
print(e.increment)

