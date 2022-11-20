for i in range(10):
    if i ==5:
        break
    print(i)
    # Else statement wont work if there is a break in side the loop
    # Else statement only works if the loop exit naturally

else:
    print("This is inside else of for")