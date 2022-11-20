num = int(input("Enter the number: "))

l = [num*i for i in range(1,11)]
print(l)

with open("mul.txt", "a") as f:
    f.write(str(l))
    f.write("\n")