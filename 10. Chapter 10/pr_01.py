class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"Name of the {self.company} Programmer is {self.name} and the Product is {self.product}")
arif = Programmer("Arif", "skype")
alka = Programmer("Alka", "Github")
arif.getInfo()
alka.getInfo()