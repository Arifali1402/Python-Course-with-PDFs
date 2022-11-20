from re import L


def div_by_5(num):
    if(num%5==0):
        return True
    else:
        return False

l = [3,5,85,124,7,54,6,4,6,5,555,505,7,6,4,56,205]
print(list(filter(div_by_5,l)))