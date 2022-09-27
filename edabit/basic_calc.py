# Create a function that takes two numbers and a mathematical operator + - / *
# and will perform a calculation with the given numbers. If the input tries to
# divide by 0, return: "Can't divide by 0!"
#
# mine:

def calculator(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Can't divide by 0!"

print(calculator(10, "+", 5))  # 15
print(calculator(10, "-", 5))  # 5
print(calculator(10, "*", 5))  # 50
print(calculator(10, "/", 5))  # 2.0

