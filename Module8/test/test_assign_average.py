import unittest

from Module8.more_fun_with_collections.assign_average import switch_average


class MyTestCase(unittest.TestCase):
    def test_switch_average_A(self):
        self.assertEqual(switch_average(), 'a')

    def test_switch_average_B(self):
        self.assertEqual(switch_average(), 'b')

    def test_switch_average_C(self):
        self.assertEqual(switch_average(), 'c')

    def test_switch_average_D(self):
        self.assertEqual(switch_average(), 'd')

    def test_switch_average_E(self):
        self.assertEqual(switch_average(), 'e')

    def test_switch_average_F(self):
        self.assertEqual(switch_average(), -1)


if __name__ == '__main__':
    unittest.main()
