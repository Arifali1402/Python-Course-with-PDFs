words = ["kaddu","kutta", "mota","chutiya", "loru"]
with open("sample3.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "$$$$$")

with open("sample3.txt","w") as f:
     f.write(content)
