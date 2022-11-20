import random
randNo = random.randint(1,100)
# print(randNo)
guess = 0
num = None
while(randNo!= num):
    guess+=1
    num = int(input("Enter your Guess: "))
    if(num>randNo):
        print("LOWER NUMBER PLEASE!!!")
    elif(num<randNo):
        print("HIGHER NUMBER PLEASE!!!")
    else:
        print("You Have Guessed It Right..Congratulations!!")
        print(f"Total no of Guesses: {guess}")



with open("highscore.txt", "r") as f:
        hiscore = int(f.read())

if(guess<hiscore):
    print("You Have just Broken the RECORD!!")
    with open("highscore.txt", "w") as f:
        f.write(str(guess))