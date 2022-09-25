"""File I/O: Replacing the word 'Python' with 'C' in a string from a file"""

filename = 'text_files/learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    # lines = [line.replace('Python', 'C') for line in lines]
    # print(lines)

    for line in lines:
        print(line.replace('Python', 'C').strip())

