class Employee:
    company = "Bharat Gas"
    salary = 5600
    salarybonus = 400
    # totalSalary = 6100 
    # Internally a property but acts as an attribute of the class
    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter
    def totalSalary(self,val):
        self.salarybonus = val - self.salary

e = Employee()
# print(e.totalSalary())
print(e.totalSalary)
e.totalSalary = 5800
print(e.salary)
print(e.salarybonus)
