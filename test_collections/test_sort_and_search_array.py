import unittest
import array as arr

from fun_with_collections.sort_and_search_array import sort_array, search_array


class MyTestCase(unittest.TestCase):
    def test_sort(self):
        test_array = arr.array('i', [-4, 2, 3, 45, 50, 66, 99])
        self.assertEqual(sort_array(), test_array)

    def test_search(self):
        self.assertEqual(search_array(), False)


if __name__ == '__main__':
    unittest.main()
