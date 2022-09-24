# https://pymotw.com
# https://pymotw.com/3/asyncio/

# https://pymotw.com/3/random/index.html

import random

for i in range(5):
    print('%04.3f' % random.random(), end=' ')
print()

# uniform() gives random floating-point number btwn passed min and max values.
for i in range(5):
    print('{:04.3f}'.format(random.uniform(1, 100)), end=' ')
print()


# seed() initializes the random number generator with expected values.
random.seed(1)

for i in range(5):
    print('{:04.3f}'.format(random.random()), end=' ')
print()

# saving state with getstate() and setstate()
import os
import pickle

if os.path.exists('state.dat'):
    # restore previously saved state
    print("Found state.dat, initializing random module")
    with open('state.dat', 'rb') as f:
        state = pickle.load(f)
    random.setstate(state)
else:
    # use a well-known starting state
    print("No state.dat. Seeding")
    random.seed(1)


import itertools
FACE_CARDS = ('J', 'Q', 'K', 'A')
SUITS = ('H', 'D', 'C', 'S')


def new_deck():
    return [
        # Always use 2 places for the value, so the strings
        # are a consistent width.
        '{:>2}{}'.format(*c)
        for c in itertools.product(
            itertools.chain(range(2, 11), FACE_CARDS),
            SUITS,
        )
    ]


def show_deck(deck):
    p_deck = deck[:]
    while p_deck:
        row = p_deck[:13]
        p_deck = p_deck[13:]
        for j in row:
            print(j, end=' ')
        print()


# Make a new deck, with the cards in order
deck = new_deck()
print('Initial deck:')
show_deck(deck)

# shuffle the deck
random.shuffle(deck)
print('\nShuffled deck:')
show_deck(deck)