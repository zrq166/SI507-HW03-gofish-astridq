import unittest

from cards import Deck
from cards import Card


class Hand(object):
    # create the Hand with an initial set of cards
    # param: a list of cards
    def __init__(self, init_cards):
        self.handcards = []
        for c in init_cards:
            self.handcards.append(c)

    # add a card to the hand
    # silently fails if the card is already in the hand
    # param: the card to add
    # returns: nothing
    def add_card(self, card):
        if card not in self.handcards:
            self.handcards.append(card)

    # remove a card from the hand
    # param: the card to remove
    # returns: the card, or None if the card was not in the Hand
    def remove_card(self, card):
        if card not in self.handcards:
            return None
        else:
            self.handcards.remove(card)
            return card

    # draw a card from a deck and add it to the hand
    # side effect: the deck will be depleted by one card
    # param: the deck from which to draw
    # returns: nothing

    def draw(self, deck):
        card = deck.pop_card()
        self.add_card(card)


class TestHand (unittest.TestCase):
    def test_init(self):
        deck=Deck()
        hand=Hand(deck.cards)
        self.assertTrue(hand.handcards==deck.cards)

    def testAddAndRemove(self):
        card1=Card(0,1) #Ace of Diamonds
        list1=[card1]
        hand=Hand(list1)
        card2=Card(0,2)
        hand.add_card(card2)
        self.assertIn(card2,hand.handcards)
        hand.remove_card(card2)
        self.assertNotIn(card2,hand.handcards)

    def testDraw(self):
        card1 = Card(0, 1)  # Ace of Diamonds
        list1 = [card1]
        hand = Hand(list1)  #create hand
        deck=Deck()
        num1=len(hand.handcards)
        hand.draw(deck)
        num2=len(hand.handcards)
        self.assertEqual(num1+1,num2)


if __name__ == "__main__":
	unittest.main(verbosity=2)