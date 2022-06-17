import random
pos1 = 0
pos2 = 0

ladders = {14:32, 19:31, 26:48, 11:49, 56:79, 62:88, 80:99}
snakes = {17:7, 54:34, 61:42, 64:60, 87:24, 93:73, 98:18}

def move(pos):
    dice = random.randint(1,6)
    print('You Have Rolled Dice',dice)
    pos += dice
    if pos in ladders:
        print("We Found A Ladder, Lets Move Up")
        pos = ladders[pos]
    elif pos in snakes:
        print("We Got Bitten By Snake, Lets Go Down")
        pos = snakes[pos]
    print('New position',pos)
    return pos

def start():
    global pos1,pos2
    while True:
        player1 = input('Player1 turn:\nEnter "y" to continue: ')
        if player1 == 'y':
            pos1 = move(pos1)
            if pos1 == 100:
                print('Player 1 WINS!!!')
                break
        player2 = input('Player2 turn:\nEnter "y" to continue: ')
        if player2 == 'y':
            pos2 = move(pos2)
            if pos2 == 100:
                print('Player 2 WINS!!!')
                break    

        if player1 != "y" or player2 != "y":
            print("\n Invalid input,Quit the game\n")
            break
if __name__ == '__main__':
    start()
        