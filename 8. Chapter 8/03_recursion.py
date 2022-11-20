from itertools import product
from re import U

def fact_iterative(num):
    product = 1
    for i in range(num):
        product = product * (i+1)
        
    return product

def fact_recursion(num):
    if(num==0 or num==1):
        return 1
    else:
        return num*fact_recursion(num-1)

num = int(input("Enter the Number: "))
print("Under recursive approach:",fact_recursion(num))
print("Under iterative approach:",fact_iterative(num))