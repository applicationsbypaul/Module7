"""
Program: basic_list.py
Author: Paul Ford
Last date modified: 06/21/2020
Purpose: uses inner functions to be able to
         get a list of numbers from a user
"""


def make_list():
    """
    creates a list and checks for valid data.
    :return: returns a list of 3 integers
    """
    a_list = []
    for index in range(3):
        while True:
            try:
                user_input = int(get_input())
            except ValueError:
                print('User must submit a number.')
                continue
            a_list.insert(index, user_input)
            break
    return a_list


def get_input():
    """
    Ask the user for a number
    :return: returns a string of the user input
    """
    user_input = input('Please enter a number')
    return user_input


if __name__ == '__main__':
    print(make_list())
