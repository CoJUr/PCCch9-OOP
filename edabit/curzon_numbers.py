# return True if a number, num, is a Curzon number. If 1 + 2^n is exactly
# divisible by 1 + 2n, then n is a Curzon number.


# mine:

def is_curzon(num):
    elevated = 2 ** num + 1
    multiplied = 2 * num + 1

    return elevated % multiplied == 0




# others:
# def is_curzon(num):
#     return True if (2 ** num + 1) % (2 * num + 1) == 0 else False


print(is_curzon(5))
print(is_curzon(10))
