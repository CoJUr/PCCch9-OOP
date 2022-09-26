

def count_words(filename):
    """Count the approximate # of words in a file."""

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"Sorry, the file {filename} does not exist.")
        pass   # pass can be used to ignore the error, program will continue
    else:
        #  count the approx number of words in the file
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


# filename = 'text_files/alice.txt'
# count_words(filename)

filenames = ['text_files/alice.txt', 'text_files/siddhartha.txt',
             'text_files/moby_dick.txt', 'text_files/little_women.txt']

for file in filenames:
    count_words(file)