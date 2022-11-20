from functools import reduce

l = [4,3,8,2,99,100]
val = reduce(max,l)
print(val)