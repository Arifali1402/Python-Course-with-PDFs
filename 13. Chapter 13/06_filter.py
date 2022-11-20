# Filter Syntax: list(filter(function,list))

def greater_then_5(num):
    if num>5:
        return True
    else:
        return False

g10 = lambda num: num>10

l = [1,2,3,4,5,6,7,8,9,10,12]
print(list(filter(greater_then_5,l)))
print(list(filter(g10,l)))