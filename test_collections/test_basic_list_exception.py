"""
Program: test_basic_list_exception.py
Author: Paul Ford
Last date modified: 06/21/2020
Purpose: uses inner functions to be able to
         get a list of numbers from a user
"""

import unittest
from unittest.mock import patch

from fun_with_collections.basic_list import make_list, get_input


class TestList(unittest.TestCase):
    @patch('fun_with_collections.basic_list.get_input', return_value='5')
    def test_make_list(self, input):
        self.assertEqual(make_list(), [5, 5, 5])

    @patch('fun_with_collections.basic_list_exception.get_input', return_value='ab')  # patch function for input
    def test_make_list_non_numeric(self, input):  # pass input
        with self.assertRaises(ValueError):  # this is familiar
            make_list()  # call the function!

    @patch('fun_with_collections.basic_list_exception.get_input', return_value='-1')
    def test_make_list_below_range(self):
        with self.assertRaises(ValueError):
            make_list()

    @patch('fun_with_collections.basic_list_exception.get_input', return_value='55')
    def test_make_list_above_range(self):
        with self.self.assertRaises(ValueError):
            make_list()


if __name__ == '__main__':
    unittest.main()
