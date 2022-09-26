"""
A program demonstrating using a while loop to repeatedly take user input and
append it to a file.
"""

filename = 'text_files/programming_poll.txt'

with open(filename, 'a') as file_object:
    while True:
        response = input("Why do you like programming? (type 'q' to quit): ")
        if response == 'q':
            break
        else:
            file_object.write(f"{response}\n")

