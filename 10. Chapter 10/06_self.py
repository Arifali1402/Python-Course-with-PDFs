class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

arif = Employee()
arif.salary = 100000
# if self is not given in the definition then an error will throw by saying getSalary() takes 0 positional arguments but 1 was given
# 1 means arif was given
arif.getSalary()
Employee.getSalary(arif)
# arif.getSalary() == Employee.getSalary(arif)