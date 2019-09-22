from cards import *
from cards2 import *
from cards3 import *
from extra1 import *
from random import choice

def extra2():
    player=0
    while int(player) not in [2, 3, 4]:
        player = input('Please input the number of computer players. \nPlease choose from 2,3,4. \nThe number of computer players:\n')
        try:
            player=int(player)
            if player not in [2,3,4]:
                print("Invalid input.")
            else:
                break
        except:
            print("Invalid input.")
            player=0

    print("Number of computer players:", player)

    totalDeck = Decknew()
    totalDeck.shuffle()
    handlist = totalDeck.deal(player, 7)
    players = {}
    for i in range(1,player+1):
        players[i]= Player(handlist[i-1].handcards)

    turns = 0
    deplete = False
