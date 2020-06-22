"""
Program: test_dict_membership.py
Author: Paul Ford
Last date modified: 06/22/2020
Purpose: test in_dict
"""
import unittest

from Module8.more_fun_with_collections.dict_membership import in_dict


class MyTestCase(unittest.TestCase):
    def test_in_dict_true(self):
        self.assertEqual(in_dict(), True)

    def test_in_dict_false(self):
        self.assertEqual(in_dict(), False)


if __name__ == '__main__':
    unittest.main()
