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


def greet_user():
    """Refactoring. Greet the user by name (do-one-thing rule)."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        filename = 'json_files/username.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")


# filename = 'json_files/username.json'
# try:
#     with open(filename) as f:
#         username = json.load(f)
# except FileNotFoundError:
#     username = input("What is your name? ")
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#         print(f"We'll remember you when you come back, {username}!")
# else:
#     print(f"Welcome back, {username}!")


def get_stored_username():
    """Get stored username if available."""
    filename = 'json_files/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


greet_user()
