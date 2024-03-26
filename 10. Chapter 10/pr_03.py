# No it won't change the class attribute
class Sample:
    a = "Arif" #class attribute

obj = Sample()
obj.a = "Vicky" #This will create an instance attribute
print(Sample.a) # Instance attribute will create but will not change the class attribute
print(obj.a)