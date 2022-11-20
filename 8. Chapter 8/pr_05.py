# Why None at the end
def printpattern(n):
    for i in range(n):
        print("* " * (n-i))


def pattern(num):
    i = num
    while (i>=1):
        print("* " * i)
        i -= 1


n = int(input("Enter the number of Rows: "))

print(pattern(n))
# print(printpattern(n))