dict = {
    "Fast": "In a quick Manner",
    "Arif": "A future Coder",
    "marks": [2,6,9],
    "anotherDict":{'Arif':'Fast'},
    1 : 2,
}
dict['marks'] = [45,67] # because it is mutable
print(dict['Fast'])
print(dict["Fast"])
print(dict['Arif'])
print(dict['marks'])
print(dict['anotherDict']['Arif'])
#Dictionary Methods
print(dict.keys()) # Print the keys of the dictionary
print(list(dict.keys()))
print(dict.values()) # Print the values of the dictionary
print(list(dict.values()))
print(dict.items()) # Print the (key,value) for all contents of the directory
print(list(dict.items()))
print(dict)
newdict = {
    "Brother": "Elder son",
    "Rahul" : "Chutiya",
    "Arif":"the gambler" # Over write 
}
dict.update(newdict) # updates the dictionary by adding key_value pairs from updates
print(dict)

#Very Very important
 #Similarity between .get and [] syntax .....
print(dict.get('Arif')) # Prints associated value with key Arif
print(dict['Arif'])  # Prints associated value with key Arif
 
 #Difference between .get and [] syntax .....
# print(dict.get('Arif2')) # Returns None as Arif2 is not present in the Dictionary
# print(dict['Arif2']) # Throws an error as Arif2 is not present in the Dictionary
