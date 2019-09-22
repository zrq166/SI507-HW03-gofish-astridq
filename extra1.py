import cards3


class Player:
    def __init__(self, init_cards):
        self.hand = {}  # hand.handcards[] is a list of cards (dictionary)
        self.book = 0  # how many books a player has
        for i in range(1, 14):
            self.hand[i] = []
        for cardtemp in init_cards:
            self.hand[cardtemp.rank_num].append(cardtemp)

    def update_bookstate(self):
        for i in range(1, 14):
            if len(self.hand[i]) == 4:
                self.book += 1
                self.hand[i] = []
                return True
        return False

    def check(self, cardrank1):
        if len(self.hand[cardrank1]) == 0:
            return False
        else:
            return True

    def remove(self, cardrank2):
        return self.hand[cardrank2].pop()

    def add(self, card):
        self.hand[card.rank_num].append(card)

def extra1():
    totalDeck = cards3.Decknew()
    totalDeck.shuffle()
    handlist = totalDeck.deal(2, 7)
    player1 = Player(handlist[0].handcards)
    player2 = Player(handlist[1].handcards)
    turns = 1  # turns 1 means player1,  2 means player2
    roundd = 1

    while True:
        print("* * * * * Round " + str(roundd) + " * * * * * * * ")
        print("totolDeck info")
        print("* * * * * * * * * * * * ")
        for i in totalDeck.cards:
            print(i.__str__())
        print("\n* * * * * * * * * * * * ")
        print("player1 info")
        for i in range(1, 14):
            for j in player1.hand[i]:
                print(j)
        print("book: " + str(player1.book))
        print("\n* * * * * * * * * * * * ")
        print("player2 info")
        for i in range(1, 14):
            for j in player2.hand[i]:
                print(j)
        print("book: " + str(player2.book))
        print("* * * * * * * * * * * * ")

        if (len(totalDeck.cards) == 0) & (player1.book + player2.book == 13):
            break

        if turns == 1:
        # player1 asks
            cardrank = input(
                "player1: Please choose a card rank you would like to ask the other player if they have (between 1-13):\n")
            cardrank.strip('\n')
            try:
                cardrank = int(cardrank)

            except ValueError:
                print("ValueError")
                continue

            try:
                if player2.check(cardrank):
                    turns = 1
                    for i in range(len(player2.hand[cardrank])):
                        player1.add(player2.remove(cardrank))
                else:
                    print("GO Fish\n")
                    drawcard = totalDeck.pop_card()
                    player1.add(drawcard)
                    if drawcard.rank_num == cardrank:
                        turns = 1
                    else:
                        turns = 2
            except KeyError:
                print("Key is not valid")
                continue

            if player1.update_bookstate():
                turns = 1
        
        else:
            # player2 asks
            cardrank = input(
                "player2: Please choose a card rank you would like to ask the other player if they have (between 1-13):\n")
            cardrank.strip('\n')
            try:
                cardrank = int(cardrank)
            except ValueError:
                print("ValueError")
                continue

            try:
                if player1.check(cardrank):
                    turns = 2
                    for i in range(len(player1.hand[cardrank])):
                        player2.add(player1.remove(cardrank))
                else:
                    print("GO Fish\n")
                    drawcard = totalDeck.pop_card()
                    player2.add(drawcard)
                    if drawcard.rank_num == cardrank:
                        turns = 2
                    else:
                        turns = 1

            except KeyError:
                print("Key is not valid")
                continue

            if player2.update_bookstate():
                turns = 2

        roundd += 1
    if player1.book > player2.book:
        print("player1 wins")
    elif player1.book == player2.book:
        print("Tie")
    else:
        print("player2 wins")
if __name__=='__main__':
    extra1()