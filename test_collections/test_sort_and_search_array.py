import unittest

from fun_with_collections.sort_and_search_array import sort_array, search_array


class MyTestCase(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(sort_array(), False)

    def test_search(self):
        self.assertEqual(search_array(), False)


if __name__ == '__main__':
    unittest.main()
