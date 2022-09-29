"""Demonstrating assigning a function to a variable and then calling it."""


def multiply(x, y):
    return x * y


a = 4
b = 7
operation = multiply
print(operation(a, b))

print("######")


def shout(word):
    return word + "!"


speak = shout
output = speak("Hello")
print(shout("Hello again"))
print(output)

print("######")
"""Using functions as other functions' arguments"""


def add(x, y):
    return x + y


def do_twice(func, x, y):
    return func(func(x, y), func(x, y))


a = 5
b = 10

print(do_twice(add, a, b))

print("######")
"""Using functions as other functions' arguments to test functions"""


def square(x):
    return x * x


def test(func, x):
    print(func(x))


test(square, 42)

import random

for i in range(5):
    value = random.randint(1, 6)
    print(value)

print("######")


# define a func that calculates the sum of all numbers from 0 up to its arg
def sum_to(x):
    res = 0
    for i in range(x):
        print("Putting current value " + str(i) + " into bucket")
        res += i
    return res


print("sum_to(10) expect 45: ", sum_to(10))
print("sum_to(9) expect 36: ", sum_to(9))


# use 9/5 * celsius + 32 to make a func which converts celsius to fahrenheit
def conv(c):
    f = 9 / 5 * c + 32
    return f


print("conv(0) expect 32: ", conv(0))


