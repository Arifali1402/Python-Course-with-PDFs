from xml.sax.handler import property_interning_dict


name = input("Enter the Name: ")
marks = input("Enter the Marks obtained: ")
phNo = input("Enter the Phone Number: ")

template = "The name of the student is: {}, his marks are: {} and his phone number is: {}"
output = template.format(name,marks,phNo)
print(output)