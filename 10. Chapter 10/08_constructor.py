class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):   # Constructor
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created")

    def getDetails(self):
        print(f"The name of the Employee is {self.name}")
        print(f"The salary of the Employee is {self.salary}")
        print(f"The name of the Employee is {self.subunit}")

    def getSalary(self,signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

harry = Employee("Arif", 1000,"YouTube")
# harry = Employee() # Throws an error --> missing 3 required positional arguments:
harry.getDetails()