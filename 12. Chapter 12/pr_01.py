def readFile(filename):
    try:
        with open(filename,"r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File - {filename} is not found")
        
readFile("1.txt")
readFile("2.txt")
readFile("3.txt")

# try:
#     with open("1.txt", "r") as f:
#         pass
#     with open("2.txt", "r") as g:
#         pass
#     with open("3.txt", "r") as h:
#         pass
# except Exception as e:
#     print(e)