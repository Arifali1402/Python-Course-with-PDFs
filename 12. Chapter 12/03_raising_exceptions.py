def Increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good")

a = Increment('asfs')
print(a)
