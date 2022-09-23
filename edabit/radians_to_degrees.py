# Create a function that takes an angle in radians and returns the
# corresponding angle in degrees rounded to one decimal place.
# ex: radians_to_degrees(1) ➞ 57.3

import math
import numpy as np


# math converrsion functions:
# math.degrees(x) -> convert radians to degrees
# math.radians(x) -> convert degrees to radians

# formula to calc a degree from a radian: degrees = radians*(180 / pi)
# to calc a radian from a degree: radians = degrees*(pi / 180)


def radians_to_degrees(rad):
    """Calculates the degrees represented by a given radian value."""
    degrees = rad * (180 / math.pi)

    return round(degrees, 1)


print(radians_to_degrees(1))

# degrees TO radians: using radians() from math library. returns a radian value
# radians TO degrees: use degrees() from math lib.

print(math.radians(57.3))
print(math.degrees(math.pi))

print(math.radians(180))


def radians_to_degrees(rad):
    """Calculates the degrees represented by a given radian value."""
    degrees = math.degrees(rad)

    return round(degrees, 1)


print(radians_to_degrees(math.pi))


# others:


def radians_to_degrees(rad):
    return round(math.degrees(rad), 1)


def radians_to_degrees(rad):
    return round(180 * rad / math.pi, 1)


radians_to_degrees = lambda r: round(r * 180 / 3.13159, 1)


# numpy library conversion
print("Numpy 180: ", np.radians(180)) # 3.141592653589793
