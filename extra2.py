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
    while True:
        print("* * * * * Round " + str(turns) + " * * * * * * * ")

        # Checking conditions for end game
        if (len(totalDeck.cards) == 0):
            deplete = True
            temp=0
            for i in players.values():
                temp+=i.book
            if temp==13:
                break

        # cur: current_player
        # Counting from 1
        cur=turns%player+1

        # current_player acting
        while ((turns % player + 1) == cur):
            print('Current player is player', cur)

            # To choose a victim
            victim = choice(range(1, 1 + player))
            while victim == cur:
                victim = choice(range(1, 1 + player))
            print('The chosen victim is: player', victim)

            # To determine the target rank
            temp = []
            for i in players[cur].hand.keys():
                if players[cur].hand[i] != []:
                    temp.append(i)
            if temp == []:
                # There must be no card left in the pool
                if not deplete:
                    raise RuntimeError
                else:
                    # Next player's turn
                    turns += 1
                    continue

            cardrank = choice(temp)
            print('The chosen cardrank is:', cardrank)

            # To get cards from the victim
            if players[victim].check(cardrank):
                for i in range(len(players[victim].hand[cardrank])):
                    players[cur].add(players[victim].remove(cardrank))
                print('Player', cur, 'found the target card from player ',victim)
                # Immediately update
                players[cur].update_bookstate()

                # if current players's hand is empty:
                if list(players[cur].hand.values()).count([])==13:
                    if not deplete:
                        try:
                            for i in range(7):
                                drawcard = totalDeck.pop_card()
                                players[cur].add(drawcard)
                                deplete = (len(totalDeck.cards) == 0)
                        except:
                            deplete=True

                # if victim's hand is empty:
                if list(players[victim].hand.values()).count([])==13:
                    if not deplete:
                        try:
                            for i in range(7):
                                drawcard = totalDeck.pop_card()
                                players[victim].add(drawcard)
                                deplete = (len(totalDeck.cards) == 0)
                        except:
                            deplete=True
            else:
                turns += 1
                if not deplete:
                    print("GO Fish\n")
                    drawcard = totalDeck.pop_card()
                    players[cur].add(drawcard)
                    if drawcard.rank==cardrank:
                        turns-=1
                    deplete = (len(totalDeck.cards) == 0)

                # Immediately update
                # if current players's hand is empty:
                players[cur].update_bookstate()
                if list(players[cur].hand.values()).count([])==13:
                    if not deplete:
                        try:
                            for i in range(7):
                                drawcard = totalDeck.pop_card()
                                players[cur].add(drawcard)
                                deplete = (len(totalDeck.cards) == 0)
                        except:
                            deplete=True

    # info
    for _ in range(1,player+1):
        print("player"+str(_)+" info")
        for i in range(1, 14):
            for j in players[_].hand[i]:
                print(j)
        print("book: " + str(players[_].book))
        print("\n* * * * * * * * * * * * ")

if __name__=='__main__':
    extra2()