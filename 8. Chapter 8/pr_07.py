# this = "       Arif is a good boy      "
# print(this)
# print(this.strip()) # Strip Help us to remove the unnecessary spaces from the beginning and from the end

from site import removeduppaths


def remove_and_strip(string,word):
    newStr = string.replace(word,"")
    return newStr.strip()

this = "       Arif is a good boy      "
a = remove_and_strip(this,"good")
print(a)
