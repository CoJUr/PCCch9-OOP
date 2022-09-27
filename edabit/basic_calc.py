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


# others:

def calculator(num1, operator, num2):
    if operator == '/' and num2 == 0:
        return "Can't divide by 0!"
    return eval('num1' + operator + 'num2')


def calculator(num1, operator, num2):
    if operator == "/" and num2 == 0:
        return "Can't divide by 0!"
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2
    if operator == "/":
        return num1 / num2


def calculator(num1, operator, num2):
    return "Can't divide by 0!" if num2 == 0 and operator == '/' else eval(str(num1) + operator + str(num2))


def calculator(num1, operator, num2):
    if operator == "/":
        if num2 == 0:
            return "Can't divide by 0!"
        else:
            return num1 / num2
    elif operator == "*":
        return num1 * num2
    elif operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    else:
        return "What?"


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