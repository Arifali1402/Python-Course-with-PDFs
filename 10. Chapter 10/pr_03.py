# No it wont change the class attribute
class Sample:
    a = "Arif"

obj = Sample()
obj.a = "Vicky"
print(Sample.a) # Instance attribute will create but will not change the class attribute
print(obj.a)