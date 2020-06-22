"""
Program: test_dict_membership.py
Author: Paul Ford
Last date modified: 06/22/2020
Purpose: test in_dict
"""
import unittest

from Module8.more_fun_with_collections.dict_membership import in_dict
# test dictionary
test_dict = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}


class MyTestCase(unittest.TestCase):

    def test_in_dict_true(self):
        self.assertEqual(in_dict(test_dict, 'A'), True)

    def test_in_dict_false(self):
        self.assertEqual(in_dict(test_dict, 'G'), False)


if __name__ == '__main__':
    unittest.main()
