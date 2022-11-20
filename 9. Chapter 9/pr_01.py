with open("poem.txt") as f:
    a = f.read()
    print(a)
    if "twinkle" in a:
        print("Twinkle is present")
    else:
        print("Twinkle is not present")

