"""Working with a file's contents; building a string from a file's contents"""

filename = 'text_files/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

filename = 'text_files/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))


"""Working with a file's contents: see if your birthday appears in pi"""
birthday = input("Enter your b-day in format mmddyy:")
if birthday in pi_string:
    print("Your b-day appears in the first million digits of pi!")
else:
    print("Your b-day doesn't appear in the first 1kk digits of pi. :( ")

