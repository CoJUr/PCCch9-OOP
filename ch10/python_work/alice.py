"""Handling FileNotFoundError Exceptions example, feat: encoding
open() argument"""

filename = 'alice.txt'
#
# with open(filename, encoding='utf-8') as f:
#     # encoding arg is needed when non-ascii characters are
#     present in the file, else you'll get a UnicodeDecodeError.

#     contents = f.read()

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
