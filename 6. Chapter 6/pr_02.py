sub1 = int(input("Enter the Marks for Subject 1: "))
sub2 = int(input("Enter the Marks for Subject 2: "))
sub3 = int(input("Enter the Marks for Subject 3: "))

total = (sub1+sub2+sub3)/3
print("Your Total Percentage is", total)
if(sub1>=33 and sub2 >=33 and sub3>=33 and total >=40):
    print("Congratulations!! You Have Passed The Examination\n")
else:
    print("You are Fail\n")