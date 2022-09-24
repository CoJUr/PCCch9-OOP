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