import unittest

from Module8.more_fun_with_collections.assign_average import switch_average


class MyTestCase(unittest.TestCase):
    def test_switch_average_A(self):
        self.assertEqual(switch_average('A'), 'a')

    def test_switch_average_B(self):
        self.assertEqual(switch_average('B'), 'b')

    def test_switch_average_C(self):
        self.assertEqual(switch_average('C'), 'c')

    def test_switch_average_D(self):
        self.assertEqual(switch_average('D'), 'd')


# def test_switch_average_E(self):
#     self.assertEqual(switch_average(), 'e')

# def test_switch_average_F(self):
#    self.assertEqual(switch_average(), -1)


if __name__ == '__main__':
    unittest.main()
