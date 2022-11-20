f = open("sample.txt", "r")

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

f.close()