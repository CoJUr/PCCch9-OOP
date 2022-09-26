"""
Add together numbers from captured user input, catching any ValueError caused
by non-numeric input.
"""


def add_numbers():
    """Add together numbers from captured user input"""


while True:
    first_number = input("Enter a number:")
    second_number = input("Enter another number please:")

    if first_number == 'q' or second_number == 'q':
        break
        
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Non-numeric input detected, please try again.")
    else:
        print(answer)

add_numbers()
