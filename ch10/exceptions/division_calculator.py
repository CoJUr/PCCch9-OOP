# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")


print("Give me two numbers to divide.")
print("enter 'q' to quit.")

while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("Second number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero! Please try again.")
    else:  # if no exception is raised, run this block.
        print(answer)
