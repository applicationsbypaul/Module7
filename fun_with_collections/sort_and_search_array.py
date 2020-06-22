"""
Program: sort_and_search_array.py
Author: Paul Ford
Last date modified: 06/21/2020
Purpose: working with array
"""
import array as arr


def sort_array():
    """
    creates an array and sorts it.
    :return: sorted array
    """
    a_list = [2, 45, 3, 66, -4, 50, 99]
    a_list.sort()
    a = arr.array('i', a_list)
    # i was not able to sort the array but only the list
    return a


def search_array(object):
    """
    searches for the object in the array.
    :param object: The key we are looking for in the array
    :return: the index of the object if it exist in the array
             if not returns -1
    """
    array = arr.array('i', [2, 45, 3, 66, -4, 50, 99])
    try:
        return array.index(object)
    except ValueError:
        print('Value not found')
        return -1


if __name__ == '__main__':
    print(search_array(-1))
    print(sort_array())

