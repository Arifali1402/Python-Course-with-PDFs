class Animals:
    animalType = "mammal"

class Pets(Animals):
    color = "white"

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bhow Bhow!!")

d = Dog()
d.bark()

