# write a function that finds the max range of a triangle's third edge,
# where the side lengths are all integers.  e.g.: 8, 10 -> 17   5, 7 -> 11
# side1 + side2 -1 = max range of third edge

def next_edge(side1, side2):
    return side1 + side2 - 1


# others:
def next_edge(*args):
    return sum(args) - 1


# next_edge = lambda a, b: a + b - 1


# farmer problem: chickens, cows, pigs with 2, 4 4 legs, respectively.
# how many legs are there in total?

# mine:
def animals(chickens, cows, pigs):
    return (chickens * 2) + (cows * 4) + (pigs * 4)


# others:
def animals(chicken, cow, pig):
    return chicken * 2 + (cow + pig) * 4


animals = lambda c, m, p: c * 2 + m * 4 + p * 4


# power calculator. take voltage and current and return the calculated power.
# eg 230, 10 -> 2300   110, 3 -> 330

# mine:
def circuit_power(voltage, current):
    return voltage * current


# others:
circuit_power = int.__mul__

circuit_power = lambda v, c: v * c
