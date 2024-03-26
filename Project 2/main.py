import random
randNo = random.randint(1,100)
print(randNo)
guess = 0
num = None
while(randNo != num):
    num = input("Enter your Guess: ")
    try:
        num = int(num)
        guess+=1
        if(num>randNo):
            print("LOWER NUMBER PLEASE!!!")

        elif(num<randNo):
            print("HIGHER NUMBER PLEASE!!!")

        else:
            print("You Have Guessed It Right..Congratulations!!")
            print(f"Total no of Guesses: {guess}")
    except Exception as e:
        print("Please Enter a Valud Number")


with open("highscore.txt", "r") as f:
    hiscore = f.read()
            
    if(hiscore == ""):
        print(f"You have set the Record of {guess} in this game")
        with open("highscore.txt", "w") as f:
            f.write(str(guess))
    elif(guess<int(hiscore)):
        print("You Have just Broken the RECORD!!")
        with open("highscore.txt", "w") as f:
            f.write(str(guess))