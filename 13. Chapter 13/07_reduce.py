from functools import reduce

sum = lambda a,b:a+b
# greater = lambda a,b:a>b
def greater(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2
l = [4,3,8,2]
val = reduce(sum,l)
val2 = reduce(greater,l)
print(val)
print(val2)
