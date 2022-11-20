from re import I
content = True
i = 1
with open("log.txt", "r") as f:
    while content:
        content = f.readline()
        if 'python' in content.lower():
            print(content)
            print(f"Yes python is present in the Log file at line number {i}")
        i+=1