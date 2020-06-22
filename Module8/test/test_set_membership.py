"""
Program: test_set_membership.py
Author: Paul Ford
Last date modified: 06/22/2020
Purpose: using sets for the first time
"""
import unittest

from Module8.more_fun_with_collections.set_membership import in_set


class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):
        self.assertEqual(in_set({1, 2, 3, 4, 5, 6, 7, 8, 9}), True)

    def test_in_set_false(self):
        self.assertEqual(in_set({1, 2, 3, 4, 5, 6, 7, 8, 9}), False)


if __name__ == '__main__':
    unittest.main()
