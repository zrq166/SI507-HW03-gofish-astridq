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

if __name__=='__main__':
    extra1()