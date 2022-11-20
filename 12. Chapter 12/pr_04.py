try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = a/b
    print(f"a/b = {c}")
except ZeroDivisionError:
    print("a/b = Infinite")