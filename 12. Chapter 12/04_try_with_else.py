from re import I


try:
    i = int(input("Enter a number: "))
    c = 1/i
    print(c)
except Exception as e:
    print(e)

else:
    print("We were successful")