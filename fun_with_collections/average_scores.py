"""
Program: average_scores.py
Author: Paul Ford
Last date modified: 06/21/2020
Purpose: Learn how to use args and kwargs
"""
import statistics


def average_scores(*args, **kwargs):
    """
    Builds a string to output attribute given by the user
    will calculate average of the scores submitted.
    :param args: scores by the user
    :param kwargs: attributes by the user
    :return:
    """
    output = 'Result: '
    for key, value in kwargs.items():
        output += ("%s = %s " % (key, value))
    # Use *args for average calculation
    output += 'with current average ' + str(statistics.mean(args))
    return output


if __name__ == '__main__':
    print(average_scores(4, 3, 2, 4, name='Michelle', courseName='Python', gpa='3.5'))
    print(average_scores(35, 75, 60, 40, user='Any', className='Biology', gpa='4.0'))
    print(average_scores(1, 100, 75, 95, ID='Paul', course='Computers', gpa=2.0))
