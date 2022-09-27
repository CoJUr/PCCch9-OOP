"""Demonstrating the use of count() method to count the number of times a word
appears in a string in a separate file."""


def counting_the(file):
    """Count the approximate # of times the word 'the' appears in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        count_of_the = contents.lower().count('the ')
        print(f"The word 'the' appears {count_of_the} times in {filename}.")


filename = 'text_files/story_of_ida.txt'
counting_the(filename)
