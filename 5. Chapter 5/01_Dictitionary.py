dict = {
    "Fast": "In a quick Manner",
    "Arif": "A future Coder",
    "marks": [2,6,9],
    "anotherDict":{'Arif':'Fast'},
    1 : 2,
}
print(dict['marks'])
dict['marks'] = [45,67] # because it is mutable
print(dict['Fast'])
print(dict['Arif']) 
print(dict['marks'])
print(dict['anotherDict'])
print(dict['anotherDict']['Arif'])
print(type(dict))