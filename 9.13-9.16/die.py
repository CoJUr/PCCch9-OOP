class Die:
    """A class representing a single die."""
    def __init__(self, sides=6):
        """Assume a six-sided die."""
        self.sides = sides

    def roll_die(self):
        """Return a random value between 1 and number of sides."""
        from random import randint
        return randint(1, self.sides)


my_die = Die()
print("Rolling a 6-sided die 10 times:")
for i in range(10):
    print(my_die.roll_die())

my_die = Die(10)
print("\nRolling a 10-sided die 10 times:")
for i in range(10):
    print(my_die.roll_die())

my_die = Die(20)
print("\nRolling a 20-sided die 10 times:")
for i in range(10):
    print(my_die.roll_die())