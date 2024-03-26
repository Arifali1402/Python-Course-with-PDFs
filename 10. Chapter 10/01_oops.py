class Number:
    def sum(self):
        return self.a + self.b 

num = Number() # Object Instantiation
num.a = 12
num.b = 34
s = num.sum()
print(s)
'''
1. PascalCase
EmployeeName -->PascalCase    [First Letter of each word should be Capital]

2. camelCase
isNumeric,isFloatOrInt-->camelCase   [First Letter of first word should be small,then first  Letter of the remaining word should be Capital]
'''