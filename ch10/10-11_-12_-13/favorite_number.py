"""
Contains one program which prompts for the user's favorite number and
stores it in a file, then another program to read the value from the file.
"""

import json


def get_and_set_favorite_number():
    """Get the user's favorite number and store it in a file."""
    filename = '../python_work/json_files/favorite_number.json'
    favorite_number = input("What is your favorite number?: ")
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)


# get_and_set_favorite_number()


def read_favorite_number():
    """Read and print out the captured favorite number from the file."""
    filename = '../python_work/json_files/favorite_number.json'
    with open(filename) as f:
        favorite_number = json.load(f)
        print(f"I know your favorite number! It's {favorite_number}.")


read_favorite_number()