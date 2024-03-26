f = open("sample2.txt", "r")

# Read first line
data = f.readline()
print(data)

# Read Second line
data = f.readline()
print(data)

# Read third line
data = f.readline()
print(data)
# and  so on
data = f.readline()
print(data)

# will print blank as there is nothing to read
data = f.readline()
print(data)
f.close()