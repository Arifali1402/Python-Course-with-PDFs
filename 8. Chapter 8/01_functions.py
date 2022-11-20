def percent(marks):
    p = ((marks[0] + marks[1] + marks[2] + marks[3])/400) * 100
    return p

marks1 = [87,90,56,99]
percentage = percent(marks1)
print(percentage)

marks2 = [85,89,59,90]
percentage = percent(marks2)
print(percentage)