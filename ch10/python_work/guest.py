"""A program which asks the user for their name and writes it to a file."""

filename = 'text_files/guest.txt'

name = input('What is your name?: ')

with open(filename, 'w') as file_object:
    file_object.write(name)

print(f"Thanks for visiting, {name}!")


filename = 'text_files/guest_book.txt'

with open(filename, 'a') as file_object:
    while True:
        name = input("what is your name? (enter 'q' to quit): ")
        if name == 'q':
            break
        else:
            print(f"Welcome, {name}!")
            file_object.write(f"{name} has visited the site.\n")

