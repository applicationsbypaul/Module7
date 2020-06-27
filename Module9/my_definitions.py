"""
Program: my_definitions.py
Author: Paul Ford
Last date modified: 06/27/2020
Purpose: creating my first python module
"""


def greeting():
    """
    A function greeting that prints a friendly greeting
    """
    print('Hello and good morning.')


def author():
    """
    A function message that prints you as the author of the code
    """
    print('Paul Ford is the author of this code')


def print_dict(dictionary):
    """
    prints key and value of dictionary 1 line at a time
    :param dictionary: dictionary that will be printed.
    """
    for item in dictionary:
        print(item, ' : ', (dictionary[item]))


def print_set(group):
    """
    Prints items in a group 1 line at a time
    :param group: a set to print
    """
    for item in group:
        print(item)
