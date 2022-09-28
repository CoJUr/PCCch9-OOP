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