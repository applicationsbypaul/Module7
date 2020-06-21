"""
Program: test_basic_list.py
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


if __name__ == '__main__':
    unittest.main()
