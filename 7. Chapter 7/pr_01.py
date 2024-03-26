num = int(input("Enter the Number: "))

for i in range(1,11):
    # print(str(num)+ "X" + str(i) + "=" + str(num*i))
    # Printing using f-string
    print(f"{num}X{i}={num*i}")
