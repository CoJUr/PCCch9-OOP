"""
A program which demonstrates reading from a file. First, the program reads the
entire contents of the file and prints them. Then, the program reads the file
by looping over the file object, printing each individual line. Last program
stores the lines in a list and then works with them outside the with block.
"""

filename = './text_files/learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()

print(contents)