class Person:
    country = "India"
    def takeBreath(self):
        print("I am Breathing...")

class Employee(Person):
    company = "Honda"
    def getSalary(self):
        print(f"Salary is {self.getSalary}")
    
    def takeBreath(self):
        print("I am an Employee so i am luckily breathing...")

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print("No salary to Programmer")
    def takeBreath(self):
        print("I am a Programmer so i am breathing++...")


p = Person()
p.takeBreath()
# print(p.company) # Throws an error

e = Employee()
e.takeBreath()
print(e.company)

pr = Programmer()
pr.takeBreath()
print(pr.company)
print(pr.country)
