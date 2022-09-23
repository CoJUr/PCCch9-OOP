# return final price from a function that takes in two arguments: price and
# discount percentage as integers.  dis(1500, 50) -> 750 dis(89, 20) -> 71.2
# answer should be rounded to two decimal places

# mine:
def dis(price, discount):
    percentage = (100 - discount) / 100

    return price * percentage


print(dis(1500, 50))


# others:
def dis(price, discount):
    """Returns the final price after discount"""

    return price - (price * (discount / 100))


def dis(price, discount):
    return round(price - (price * (discount / 100)), 2)


def dis(price, discount):
    return price * (100 - discount) * 0.01


def dis(price: int, discount: int) -> float:
    return round(price * (1 - discount / 100), 2)

