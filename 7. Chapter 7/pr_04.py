num = int(input("Enter the Number: "))
Prime = True
for i in range(2,num):
    if(num%i == 0):
        Prime = False
        break
if(Prime):
    print("This Number is Prime\n")
else:
    print("This Number is not Prime\n")
