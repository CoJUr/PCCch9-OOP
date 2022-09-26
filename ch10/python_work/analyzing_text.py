# # http://gutenberg.org is a great source of free books
#
# # split() method can be used to break a string into a list of words
#
# title = "Alice in Wonderland"
# print(title.split())
#
# filename = 'text_files/alice.txt'
#
# try:
#     with open(filename, encoding='utf-8') as f:
#         contents = f.read()
# except FileNotFoundError:
#     print(f"Sorry, the file {filename} does not exist.")
# else:
#     #  count the approx number of words in the file
#     words = contents.split()
#     num_words = len(words)
#     print(f"The file {filename} has about {num_words} words.")
