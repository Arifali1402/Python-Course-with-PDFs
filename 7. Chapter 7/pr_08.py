from sqlite3 import Row


rows = int(input("Enter the number of Rows: "))

for i in range(0,rows):
        print("* " * (i+1))