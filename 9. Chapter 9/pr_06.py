with open("log.txt", "r") as f:
    content = f.read()

if 'python' in content.lower():
    print("Yes python is present in the Log file")
else:
    print("No python is not present in the Log file")

