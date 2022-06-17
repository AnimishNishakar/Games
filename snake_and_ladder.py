import random
ladder = {5:20,10:26,16:74,36:94,28:50,70:99,60:90,80:100}
snake = {25:3,78:33,95:8,99:15}
pos1 = 0
pos2 = 0

def move(pos):
    dice = random.randint(1,6)
    print(f"Dice:{dice}")
    pos = pos + dice
    if pos in snake:
        print("Bitten by snake")
        pos = snake[pos]
        print(f"Position : {pos}")
    elif pos in ladder:
        print("Climbed the ladder")
        pos = ladder[pos]
        print(f"Position : {pos}")
    else:
        print(f"Position : {pos}")
    print("\n")
    return pos

while True:
    A = input("Player1 Enter\"A\" to throw the dice: ")
    pos1 = move(pos1)
    if pos1 >= 100:
        print("GAME OVER!!!\nPlayer1 WINS.")
        break
        
    B = input("Player2 Enter\"B\" to throw the dice: ")
    pos2 = move(pos2)
    if pos2 >= 100:
        print("GAME OVER!!!\nPlayer2 WINS.")
        break