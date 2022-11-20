with open("file1.txt") as f:
    a = f.read()

with open("file2.txt") as g:
    b = g.read()

if a == b:
    print("Yes Files are identical")
else:
    print("No Files are not identical")
