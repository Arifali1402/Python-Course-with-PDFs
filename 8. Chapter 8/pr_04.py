def add(num):
    if(num == 1):
        return num
    else:
        return num + add(num-1)

num = int(input("Enter the Limit: "))
s = add(num)
print(f"The Sum Of First {num} Natural Number is {s}")


