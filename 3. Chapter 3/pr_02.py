from sqlite3 import Date
from unicodedata import name

letter = '''Dear <|NAME|> ,
Greetings from XYZ coding house, I am happy to tell you about your selection.
You Are Selected!!!!
Have a Great Day pal.
Thanks and Regards,
Bill
<|DATE|>'''
print(letter)
name = input("Input the name: ")
date = input("Enter the date: ")  
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)