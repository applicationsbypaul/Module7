def switch_average(key):
    """
    Try to implement a switch
    So it tries to see if the key is in the dictionary
    if not does the except KeyError which would be the default
    :param key: The key we are searching for in the dictionary
    :return: This is good.
    """
    # test dictionary
    dict_test = {'A': 'a', 'B': 'b', 'C': 'C', 'D': 'd', 'E': 'e'}
    try:
        result = dict_test[key]
    except KeyError:
        result = -1
    return result


if __name__ == '__main__':
    print(switch_average('F'))
