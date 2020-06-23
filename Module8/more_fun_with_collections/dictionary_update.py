"""
Program: dictionary_update.py
Author: Paul Ford
Last date modified: 06/22/2020
Purpose: using dictionaries to gather
         store and recall info
"""


def get_test_scores():
    """
    Gathers test scores for a user and stores them
    into a dictionary.
    :return: scores_dict a dictionary of scores
    """
    scores_dict = dict()
    num_scores = int(input('Please how many test scores are going to be entered: '))
    key_values = 'score'  # this value will be the key for the dictionary incrementing by 1
    for key in range(num_scores):
        while True:
            try:
                # ask the user for new data since the function data was bad
                score = int(input('Please enter your test score: '))
                scores_dict.update({key_values + str(key + 1): score})
                if int(score < 0) or int(score > 100):
                    raise ValueError
            except ValueError:
                print('Test score has to be between 1 and 100.')
                continue
            else:
                break
    return scores_dict


def average_scores(dictionary):
    """
    Recall the scores from the dictionary
    adding them to total calculate the average
    :param dictionary: a dictionary of scores
    :return: returns the average score.
    """
    total = 0  # local variable to calculate total
    key_values = 'score'
    for score in range(len(dictionary)):
        total += dictionary[key_values + str(score + 1)]
    return round(total / len(dictionary), 2)


if __name__ == '__main__':
    pass
