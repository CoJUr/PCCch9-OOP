# with open('text_files/pi_digits.txt') as file_object:
#     # open() returns an object representing the file stored in file_object.
#     # 'with' closes the file automatically. close() not needed.
#     contents = file_object.read()  # read() reads the entire file into a str.
# print(contents.rstrip())  # rstrip() removes the extra blank line at the end

# Absolute file path:
file_path = '/Users/cojur/Desktop/playground/PCCch9-OOP/ch10/python_work/text_files/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
print(contents.rstrip())


