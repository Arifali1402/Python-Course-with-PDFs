score = int(input("Enter Your Marks: "))

if score>=90:
    grade = "Ex"
elif score>=80:
    grade = "A"    
elif score>=70:
    grade = "B"
elif score>=60:
    grade = "C"
elif score>=50:
    grade = "D"
else:
    grade = "F"

print("Your Grade is",grade)

