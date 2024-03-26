class Employee: # Base Class
    company = "Google"
    def showDetails(self):
        print("This is an employee")

class Programmer(Employee): # Child Class
    language = "Python"
    company = "YouTube" # over writing an already existing attribute
    def getLanguage(self):
        print(f"The Language is {self.language}")
    def showDetails(self): # over writing an already existing function
        print("This is a Programmer")

e = Employee()
p = Programmer()
e.showDetails()
p.showDetails()
p.getLanguage()
print(e.company)
print(p.company)
# e.getLanguage() # Throws an error.