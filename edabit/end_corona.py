"""
Write a function which takes the number daily avg recovered cases
'recovers', daily avg new cases 'new_cases', current active cases 'active_cases',
and returns the number of days it will take to reach 0 cases. Round up the
result to the nearest integer. recovers will always be greater than new_cases.
"""


# mine:
def end_corona(recovers, new_cases, active_cases):
    diff = recovers - new_cases
    days_needed = active_cases / diff

    import math

    res = math.ceil(days_needed)
    return res


# others:
from math import ceil


def end_corona(recovers, new_cases, active_cases):
    return ceil(active_cases / (recovers - new_cases))


def end_corona(recovers, new_cases, active_cases):
    count = 0
    while active_cases > 0:
        active_cases -= recovers
        active_cases += new_cases
        count += 1
    return count


def end_corona(recovers, new_cases, active_cases):
    return round(active_cases / (recovers - new_cases) + 0.5)
