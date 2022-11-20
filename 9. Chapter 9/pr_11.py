import os

oldname = "new.txt"
newname = "rename_by_python.txt"
with open(oldname, "r") as f:
    content = f.read()

with open(newname, "w") as g:
    g.write(content)
os.remove(oldname)