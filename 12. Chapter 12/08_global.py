a = 54 # Global Variable
def func1():
    global a #  This will change the value of the global variable
    print(f"Prints Statement 1: {a}")
    # Local Variable if global keyword is not used
    a = 8 
    print(f"Prints Statement 2: {a}")
    
func1()
print(f"Prints Statement 3: {a}")