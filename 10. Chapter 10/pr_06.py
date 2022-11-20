# Yes it will work but is not recommended
class Sample:
    a = "Arif"
    def __init__(self,name):
        self.name = name
        # Also Works
    def __init__(arif,name):
         arif.name = name
         # Also Works
    def __init__(slf,name):
        slf.name = name


obj = Sample("Bunty")
print(obj.name)