# Python program to shuffle deck of cards

import itertools
import random

# make a deck of cards
deck = list(itertools.product(range(1, 14), [
            'Spade', 'Heart', 'Diamond', 'Club']))

# shuffle
random.shuffle(deck)

# draw 5 cards
print("You got:")
for i in range(5):
    print(deck[i][0], "of", deck[i][1])
