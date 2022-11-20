def convert(inches):
    cm = (inches*2.54)
    return cm

inch = float(input("Enter the Length in Inches: "))
a = convert(inch)
print(f"{inch} inches = {a} cm")
