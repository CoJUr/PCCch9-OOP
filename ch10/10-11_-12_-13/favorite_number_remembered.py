"""Combine functions from favorite_number.py. If the number is already stored,
print the number to the user. If not, prompt for the user's favorite number and
store it in a file."""

import json
from favorite_number import get_and_set_favorite_number, read_favorite_number


def get_stored_favorite_number():
    """Get the stored favorite number if one exists, and print it"""
    filename = '../python_work/json_files/favorite_number.json'
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        print(f"I know your favorite number! It's {favorite_number}.")

    if favorite_number:
        print(f"I know your favorite number! It's {favorite_number}.")
    else:
        get_and_set_favorite_number()
        read_favorite_number()