# create a function that takes an int and returns the factorial of that int
# ex: factorial(3) -> 6   factorial(5) -> 120
import math


# mine
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


# others
def factorial(num):
    return 1 if num < 2 else num * factorial(num - 1)


def factorial(num):
    return math.factorial(num)


def factorial(n):
    #     best case: 1! = 1
    if n == 1 or n == 0:
        return 1
    # recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)


def factorial(num):
    if num < 2:
        return num
    return num * factorial(num - 1)
