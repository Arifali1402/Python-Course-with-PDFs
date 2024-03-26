# def mulTable(num):
#     for i in range(1,11):
#         print(f"{num}X{i} = {num*i}")


# How To Remove NONE from the end?
def mulTable(num):
    i = 1
    while (i<=10):
        print(f"{num}X{i} = {num*i}")
        i+=1
        
num = int(input("Enter the Number: "))
print(f"MULTIPLICATION TABLE OF {num} is: ")
mulTable(num)
