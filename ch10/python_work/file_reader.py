with open('text_files/pi_digits.txt') as file_object:
    # open() returns an object representing the file stored in file_object.
    # 'with' closes the file automatically after the block of code is executed.
    contents = file_object.read()  # read() reads the entire file into a str.
print(contents.rstrip())  # rstrip() removes the extra blank line at the end

# Absolute file path version:
# file_path = '/Users/cojur/Desktop/playground/PCCch9-OOP/ch10/python_work/text_files/pi_digits.txt'
# with open(file_path) as file_object:
#     contents = file_object.read()
# print(contents.rstrip())


#           Reading line by line:
# might want to look for any line that contains a certain string. can use a for
# loop to iterate through the file object.

filename = 'text_files/pi_digits.txt'

with open(filename) as file_object:
    print("\nReading line by line:")
    for line in file_object:
        print(line.rstrip())


#           Making a list of lines from a file:
filename = 'text_files/pi_digits.txt'

print("\nMaking a list of lines from a file with readlines():")
with open(filename) as file_object:
    lines = file_object.readlines()
    # readlines() puts lines to a list for processing outside the with block.

for line in lines:
    print(line.rstrip())
