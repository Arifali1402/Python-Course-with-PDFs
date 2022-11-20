# Alternate

def Maximum(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3     


def Greatest_Number(n1, n2, n3):
    if(n1>n2 and n1>n3):
        return n1
    elif(n2>n3):
        return n2
    else:
        return n3

num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num2: "))
num3 = int(input("Enter Num3: "))

g = Greatest_Number(num1,num2,num3)
h = Maximum(num1,num2,num3)
print("Greatest among Three Numbers: "+str(g))
print(h)

    