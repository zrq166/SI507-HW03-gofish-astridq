import unittest
from cards2 import Hand
from cards import Card
from cards import Deck


class Handnew(Hand):
    def remove_pairs(self):
        i = 0
        while i < len(self.handcards):  # for i card
            j = i + 1
            while j < len(self.handcards):
                if self.handcards[i].rank == self.handcards[j].rank:
                    del self.handcards[i]
                    del self.handcards[j - 1]
                    i = i - 1
                    break
                else:
                    j = j + 1
            i = i + 1


class Decknew(Deck):
    def deal(self, num_hands, num_cards):
        handlist = []
        initial_cards = []
        for i in range(num_hands):
            temp1 = Handnew(initial_cards)
            handlist.append(temp1)
        no_card = 0  # has card in deck
        if num_cards == -1:
            while True:
                for j in handlist:
                    if len(self.cards) != 0:
                        j.draw(self)
                    else:
                        no_card = 1
                        break
                if no_card == 1:
                    break
        else:
            for i in range(num_cards):
                for j in handlist:
                    if len(self.cards) != 0:
                        j.draw(self)
        return handlist


class TestHandnew(unittest.TestCase):
    def test_remove_pairs(self):
        init_card = [Card(0, 1), Card(0, 2), Card(0, 3), Card(0, 1), Card(0, 2), Card(3, 3), Card(0, 1)]
        hand = Handnew(init_card)
        hand.remove_pairs()
        self.assertTrue((len(hand.handcards) == 1) & (hand.handcards[0].__str__() == "Ace of Diamonds"))

    def test_deal(self):
        deck1 = Decknew()
        handlist = []
        handlist = deck1.deal(3, 2)
        self.assertTrue((len(handlist) == 3) & (len(handlist[0].handcards) == 2) & (len(handlist[1].handcards) == 2) & (
                    len(handlist[2].handcards) == 2))


if __name__ == "__main__":
    unittest.main(verbosity=2)
