st = input("Enter the Comment: ")
# spam = False

# if("make a lot of money" in st):
#     spam = True
# elif("buy now" in st):
#     spam = True
# elif("subscribe this" in st):
#     spam = True
# elif("click" in st):
#     spam = True
# else:
#     spam = False

# if(spam):
#     print("This Text is Spam")
# else:
#     print("This Text is not a Spam")

# Alternate

if(st == "make a lot of money" or st =="buy now" or st == "Subscribe this" or st == "click this"):
    print("Spam Comment Detected\n")
else:
    print("No Spam Comment Detected\n")