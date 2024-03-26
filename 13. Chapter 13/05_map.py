# def square(num):
    # return num*num
square = lambda x:x*x
l1 = [1,4,8] 
# Method 1
l2 = []
for item in l1:
    l2.append(square(item))
print(l2)

# Method 2
l3 = list(map(square,l1))
print(l3)

# Method 3
tuple1 = tuple(map(square,l1))
print(tuple1)