from math import pi


# given a radius of a circle and area of a square, return True if the
# circumference of the circle is > the square perimeter, False vice versa
# can use Pi to 2 decimal places    circumference = 2PiR
# perimeter = 4s     s = side length = sqrt(area)
# ex: circle_or_square(5, 100) -> False   circle_or_square(8, 144) -> True

# mine
def circle_or_square(radius, area):
    circle_circumference = 2 * 3.14 * radius
    square_perimeter = 4 * (area ** 0.5)

    return circle_circumference > square_perimeter


# others
def circle_or_square(rad, area):
    return 2 * pi * rad > 4 * pow(area, 0.5) #from math import pi


def circle_or_square(r, s):
    return 1.57 * r > s ** 0.5


circle_or_square=lambda r, a: a ** .5 * 4 < 6.28 * r
