## Overview of today's warm-up challenge

# Obtained From:
# https://samarakoon-gayan.medium.com/a-game-of-black-jack-on-python-as-a-fun-exercise-3cd54efb9d83

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
card_names = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f'{self.value} of {self.suit}'


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for card in card_names:
                self.deck.append(Card(suit, card))

    def __str__(self):

        return f'{[value for value in self.deck if print(value)]}'

    def shuffle(self):
        # use > 1 to not shuffle a deck of 1 card
        if self.deck:
            random.shuffle(self.deck)

    def deal_single(self):
        single_card = self.deck.pop()
        return single_card


if __name__ == "__main__":
    deck = Deck()
    print('Let us play a little game')
    print(deck)