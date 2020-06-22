import unittest

from fun_with_collections.sort_and_search_list import search_list, sort_list


class MyTestCase(unittest.TestCase):
    def test_search_list(self):
        self.assertEqual(search_list(55), 2)

    def test_search_list(self):
        [6, 3, 12, 11, -85]
        self.assertEqual(sort_list(), [-85, 3, 6, 11, 12])


if __name__ == '__main__':
    unittest.main()
