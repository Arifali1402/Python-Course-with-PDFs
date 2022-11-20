a = 54 # Global Variable
def func1():
    global a
    print(f"Prints Statement 1: {a}")
    a = 8 # Local Variable if global keyword is not used
    print(f"Prints Statement 2: {a}")
    
func1()
print(f"Prints Statement 3: {a}")

