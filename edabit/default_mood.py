"""
Function that takes in a 'mood' and returns a sentence saying "Today, I am
feeling {mood}". If no arg is passed, return "Today, I am feeling neutral".
"""


# mine:
def mood_today(mood="neutral"):
    return "Today, I am feeling " + mood


print(mood_today("happy"))
print(mood_today("sad"))
print(mood_today())


# others:
def mood_today(*mood):
    if len(mood) != 0:
        return "Today, I am feeling {}".format(*mood)
    else:
        return "Today, I am feeling neutral"


def mood_today(*mood):
    # return "Today, I am feeling {}".format(mood[0] if mood else 'neutral')
    return 'Today, I am feeling '+mood if mood else 'Today, I am feeling neutral'


def mood_today(*mood):
    if len(mood) != 0:
        return "Today, I am feeling "+ mood[0]
    else:
        return "Today, I am feeling neutral"