# Use open function to read the content of a file

# f = open("sample.txt", "r")
f = open("sample.txt") # By default the mode is "r"
data = f.read()
# data = f.read(3) # Reads the first 3 characters of the file
print(data)
# Close the file
f.close()