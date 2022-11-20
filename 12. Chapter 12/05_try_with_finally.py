try:
    i = int(input("Enter a number: "))
    c = 1/i
    print(c)
except Exception as e:
    print(e)
    exit()
finally:
    print("We are done")

print("Thanks For using the program")