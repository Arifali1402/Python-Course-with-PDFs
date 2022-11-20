def game():
    return 9

score = game()

with open("high_score.txt", "r") as f:
    hiscoreStr = f.read()
    
if hiscoreStr=="":
    with open("high_score.txt", "w") as f:
        f.write(str(score))

elif int(hiscoreStr)<score:  
    with open("high_score.txt", "w") as f:
        f.write(str(score))