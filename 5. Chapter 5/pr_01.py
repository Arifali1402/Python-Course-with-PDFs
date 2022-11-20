from pathlib import PureWindowsPath
myDict = {
    "Pankha": "fan",
    "Dabba" : "Box",
    "Vastu" : "Item"
}
print("Options Are", myDict.keys())
a = input("Enter the Hindi Word: ")

print("The meaning of the word in hindi is:",myDict.get(a)) # To Avoid Error