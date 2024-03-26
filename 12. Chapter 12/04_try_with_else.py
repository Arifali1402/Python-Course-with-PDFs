try:
    i = int(input("Enter a number: "))
    c = 1/i
    print(c)
except Exception as e:
    print(e)

# This will execute only when the try gets executed
else:
    print("We were successful")