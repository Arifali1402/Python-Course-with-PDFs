# Multiple Inheritance
class Employee:
    company = "Visa"
    eCode = 120

class Freelancer:
    company = "Fiverr"
    level = 0

    def upgrade_level(self):
        self.level += 1

class Programmer(Freelancer, Employee):
    name = "Rahul"

p = Programmer()
print(p.level)
p.upgrade_level()
print(p.level)
print(p.eCode)
print(p.name)
print(p.company) # prints the property which is written in the first place