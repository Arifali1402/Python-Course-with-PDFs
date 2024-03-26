while(True):
    print("Press 'q' to quit..")
    a = input("Enter a number: ")
    if a == 'q':
        break
    try:
        print("Trying")
        a = int(a)
        if a >6:
            print("Number is greater than 6") # Throws a value error if input is something other than input
    except Exception as e:
        print(f"Your input resulted in an error: {e}")
        # print(e)
print("Thanks For Playing the game...")