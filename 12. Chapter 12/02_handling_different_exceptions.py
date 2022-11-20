try:
    a = int(input("Enter a number: "))
    c = 1/a
    print(c)
except ValueError as e:
    print(" enter a valid value.")
    # print(e)
except ZeroDivisionError as e:
    print("Make Sure you are not dividing by 0 ")
    # print(e)

print("Thanks For using this code")
