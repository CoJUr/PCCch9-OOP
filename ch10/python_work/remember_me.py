# """
# Saving and reading user-generated data so that data persists between
# sessions utilizing json.dump() and json.load() functions.
# """
"""
Combining the programs from greet_user.py and remember_me.py to
retrieve the username from memory if possible. If the file doesn't exist,
prompt user for a username and store it in username.json utilizing a
try-except block.
"""

import json

# load username if its stored already, else prompt for it and store it
filename = 'json_files/username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")

