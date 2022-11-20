class Number:
    def sum(self):
        return self.a + self.b 

num = Number() # Object Instantiation
num.a = 12
num.b = 34
s = num.sum()
print(s)
'''
PascalCase
EmployeeName -->PascalCase    [First Letter of the word should be Capital]

camelCase
isNumeric,isFloatOrInt-->camelCase   [First Letter of the word should be small and second Letter of the word should be Capital]
'''