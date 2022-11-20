from tkinter import N


class Calculator:
    def __init__(self,num):
        self.number = num
    def square(self):
        print(f"The Square of {self.number} is {self.number **2}")
    def cube(self):
        print(f"The Cube of {self.number} is {self.number **3}")
    def SquareRoot(self):
        print(f"The Square Root of {self.number} is {self.number **0.5}")

n = int(input("Enter the Number: "))
a = Calculator(n)
a.square()
a.cube()
a.SquareRoot()
