class Calculator:
    def __init__(self,num):
        self.number = num
    def square(self):
        print(f"The Square of {self.number} is {self.number **2}")
    def cube(self):
        print(f"The Cube of {self.number} is {self.number **3}")
    def SquareRoot(self):
        print(f"The Square Root of {self.number} is {self.number **0.5}")

    @staticmethod
    def greet():
        print("****** Hello Sir, Welcome to the best calculator in the World ******")

n = int(input("Enter the Number: "))
a = Calculator(n)
a.greet()
a.square()
a.cube()
a.SquareRoot()