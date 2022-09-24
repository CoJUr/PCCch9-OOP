from random import randint
from random import choice

print(randint(1, 6))

players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)  # choice() takes a list or tuple
print(first_up)
