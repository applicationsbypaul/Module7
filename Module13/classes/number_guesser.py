"""
Program: NumberGuesser.py
Author: Paul Ford
Last date modified: 07/11/2020
Purpose: creates an object for the game
         it will put your guesses in a
         list until you get the right one.
"""


class NumberGuesser:

    def __init__(self):
        """
        class attribute contains all the guessed numbers
        should be empty on new game or reset game
        """
        self.guessed_list = []

    def add_guess(self, num):
        """
         class method that will add to the guessed_list
        :param num: guessed number
        """
        self.guessed_list.append(num)
