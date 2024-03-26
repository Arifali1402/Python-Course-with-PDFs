# We can comment out the constructor of the EMployee class but still the super() operator will work but this is not same in case of other class methods
class Person:
    country = "India"

    def __init__(self):
        print("Initialising Person...\n")

    def takeBreath(self):
        print("I am Breathing...")


class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()
        print("Initialising Employee...\n")

    def getSalary(self):
        print(f"Salary is {self.getSalary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so i am luckily breathing...")


class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
        super().__init__()
        print("Initialising Programmer...\n")

    def getSalary(self):
        print("No salary to Programmer")

    def takeBreath(self):
        super().takeBreath()
        print("I am a Programmer so i am breathing++...")


pr = Programmer()
pr.takeBreath()