#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 08:05:59 2019

@author: lx
"""

class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]


    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank


    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])  
    
    def cmp(self, other):
        # Check the suits
        if self.suit > other.suit: 
            return 1
        if self.suit < other.suit: 
            return -1
        # Suits are the same... check ranks
        if self.rank > other.rank: 
            return 1
        if self.rank < other.rank: 
            return -1
        # Ranks are the same... it's a tie
        return 0
    
    def __eq__(self, other):
        return self.cmp(other) == 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __ne__(self, other):
        return self.cmp(other) != 0

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))


    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + "\n"
        return s


    def shuffle(self):
        import random
        rng = random.Random()        # Create a random generator
        rng.shuffle(self.cards)      # uUse its shuffle method

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False


    def pop(self):
        return self.cards.pop()

    
    def is_empty(self):
        return self.cards == []

red_deck = Deck()
red_deck.shuffle()
blue_deck = Deck()

print(red_deck)

#three_of_clubs = Card(0, 3)
#card1 = Card(1, 11)
#print(three_of_clubs)
#print(card1)

#card1 = Card(1, 11)
#card2 = Card(1, 3)
#card3 = Card(1, 11)
#print(card1 < card2)
#print(card1 == card3)