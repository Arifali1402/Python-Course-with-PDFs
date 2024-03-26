import random

# Similar to ROCK,PAPER And SCISSOR
    
def gameWin(comp,you):
    if comp == you:
        return None
        
    elif comp=='s':
        if you == 'g':
            return True
        elif you == 'w':
            return False

    elif comp=='w':
        if you == 's':
            return True
        elif you == 'g':
            return False
    elif comp=='g':
        if you == 'w':
            return True
        elif you == 's':
            return False

print("Comp Turn: Snake(s) Water(w) or Gun(g)")
randNo = random.randint(1,3)
# print(randNo)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'
you = input("Your Turn: Snake(s) Water(w) or Gun(g): ")
if(you in ['s','w','g']):
    print(f"Computer Chose: {comp}")
    print(f"You Chose: {you}")
    a = gameWin(comp,you)
    if(a == None):
        print("The Game has ended in a Tie!")
    elif(a):
        print("YOU WIN!")    
    else:
        print("YOU LOSE!")
else:
    print("Invalid Choice.. You Lose!!")

