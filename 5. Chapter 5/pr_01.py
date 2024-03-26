myDict = {
    "Pankha": "Fan",
    "Dabba" : "Box",
    "Vastu" : "Item"
}
print("Options Are", list(myDict.keys()))
a = input("Enter the Hindi Word: ")

if(myDict.get(a) == None):
    print("The Hindi Word of",a,"does not exist in the Given Dictionary")

else:
    print("The meaning of the word in hindi is:",myDict.get(a)) # To Avoid Error