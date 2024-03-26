a = [2,5,3,56,8,9,6,67,89,34,73,45,67,43,25,6]
print(a)
# b = []
# for item in a:
#     if(item%2==0):
#         b.append(item)
# print(b)

# Short Cut to write the Same:
b = [i for i in a if i%2==0]
print(b)

t = [1,4,2,1,4,3,5,3,5,3,1]
s = {i for i in t}
print(s)

l1 = [i for i in a if i%3==1]
print(l1)