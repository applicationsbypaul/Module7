"""
Program: date_time_assignment.py
Author: Paul Ford
Last date modified: 06/23/2020
Purpose: Gives the half birthday
"""
from datetime import datetime, timedelta

recent_birthday = datetime(2020, 5, 21)
# half birthday I looked up to be 182 days
half_birthday_length = 182


def half_birthday(birthday):
    """
    returns the users half birthday
    in datetime format
    :param: birthday is the user birthday in timedate format
    :return: return the users half birthday
    """
    return birthday + timedelta(days=half_birthday_length)


if __name__ == '__main__':
    print(half_birthday(recent_birthday))
