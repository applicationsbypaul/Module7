"""
Program: dictionary_ops.py
Author: Paul Ford
Last date modified: 06/27/2020
Purpose: creates a module greetings
         in pkg definitions
"""


def print_dict(dictionary):
    """
    prints key and value of dictionary 1 line at a time
    :param dictionary: dictionary that will be printed.
    """
    for item in dictionary:
        print(item, ' : ', (dictionary[item]))
