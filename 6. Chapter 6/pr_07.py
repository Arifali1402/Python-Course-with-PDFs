# string.lower()
#Some methods for Case_insenstivity
# string.upper()
# string.casefold() -->Strongest
name = "Harry"
st = input("Enter the String: ")

if(name.lower() in st.lower()):
    print("YES, This post is Talking about", name)
else:
    print('''No, The string does not contain anything related to the name''', name)