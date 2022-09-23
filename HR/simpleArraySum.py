# sum the elements of an array
# https://www.hackerrank.com/challenges/simple-array-sum/problem
# mine:
# def simpleArraySum(ar):
#     """Returns the sum of the elements of an array"""
#     sum = 0
#
#     for el in ar:
#         sum += el
#
#     return sum


# others:
def simpleArraySum(n, ar):
    return sum(ar)

print(simpleArraySum(6, [1, 2, 3, 4, 10, 11]))