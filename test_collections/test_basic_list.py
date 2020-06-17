import unittest
from unittest.mock import patch

from fun_with_collections.basic_list import make_list


class TestList(unittest.TestCase):
    @patch('fun_with_collections.topic1.get_input', return_value='5')
    def test_make_list(self, input):
        self.assertEqual(make_list(), [2, 54, 28])


if __name__ == '__main__':
    unittest.main()
