"""
Program: sort and search_list.py
Author: Paul Ford
Last date modified: 06/21/2020
Purpose: sort and search list.
"""


def search_list(object):
    """
    Searches for object in list, if not there returns -1
    if object is there return the index.
    :param object: is the parameter looked for in the list
    :return: the index of the where the object is
    """
    a_list = [1, 3, 55, 99]
    try:
        # need to return index or negative 1 so both need a return
        return a_list.index(object)
    except ValueError:
        return -1


def sort_list():
    """
    Sorts the list and then returns it.
    :return:
    """
    # just return the list since sort does it to the object.
    a_list = [6, 3, 12, 11, -85]
    a_list.sort()
    return a_list


if __name__ == '__main__':
    pass
