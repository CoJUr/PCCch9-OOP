"""
Demonstrating writing to an empty file passing to open() 'w' for write mode
Other modes explored: 'r' (read mode), 'a' (append mode), 'r+' read and write)
"""

filename = 'text_files/programming.txt'

# call open() with a second argument 'w' (write mode) to write to the file.
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
    file_object.write(str(49332148 + 594958))  # write() only accepts str args.


print("~~~~       Appending to the file:         ~~~~~")
with open(filename, 'a') as file_object:
    file_object.write("\nI also love finding meaning in large datasets.\n")
    file_object.write("I <3 creating apps that run in browser.\n")



