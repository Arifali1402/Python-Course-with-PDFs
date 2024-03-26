def Increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good")

# a = Increment(76)
# print(a)
a = Increment('asfs')
print(a)
