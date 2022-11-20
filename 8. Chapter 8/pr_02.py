def convert(celcius):
    farhenite = ((9/5) * celcius)+32
    return farhenite

cel = float(input("Enter the temperature in Celcius: "))

temp = convert(cel)
print(f"{cel} CELCIUS = {temp} FARHENITE\n")
