dict = {
    "Fast": "In a quick Manner",
    "Arif": "A future Coder",
    "marks": [2,6,9],
    "anotherDict":{'Arif':'Fast'},
    1 : 2,
}

#Dictionary Methods
print(dict.keys()) # Print the keys of the dictionary
print(list(dict.keys()))
print(dict.values()) # Print the values of the dictionary
print(list(dict.values()))
print(dict.items()) # Print the (key,value) for all contents of the directory
print(list(dict.items()))
print(dict)
newDict = {
    "Brother": "Elder son",
    "Rahul" : "Chutiya",
    "Arif":"the gambler" # Overwrite the value of the key in the dictionary
}
dict.update(newDict) # updates the dictionary by adding key_value pairs from newDict
print(dict)

#Very Very important
#Similarity between .get and [] syntax .....
print(dict.get('Arif')) # Prints associated value with key 'Arif'
print(dict['Arif'])  # Prints associated value with key 'Arif'
 
#Difference between .get and [] syntax .....
# print(dict.get('Arif2')) # Returns None as Arif2 is not present in the Dictionary
# print(dict['Arif2']) # Throws an error as Arif2 is not present in the Dictionary