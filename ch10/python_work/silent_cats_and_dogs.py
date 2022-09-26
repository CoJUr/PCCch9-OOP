"""A program that reads cats and dog names, and then
prints them to the screen while handling possible FileNotFound error."""

filename1 = 'text_files/cats.txt'
filename2 = 'text_files/dogs.txt'

try:
    with open(filename1) as f1:
        cats = f1.readlines()
except FileNotFoundError:
    # print(f"Sorry, the file {filename1} does not exist.")
    pass
else:
    for cat in cats:
        print(cat.rstrip())


try:
    with open(filename2) as f2:
        dogs = f2.readlines()
except FileNotFoundError:
    # print(f"Sorry, the file {filename2} does not exist.")
    pass
else:
    for dog in dogs:
        print(dog.rstrip())

