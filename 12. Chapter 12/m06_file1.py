def greet(name):
    print(f"good Morning {name}")

print(__name__)
if __name__ == "__main__":
    n = input("Enter a name: ")
    greet(n)