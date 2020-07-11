import unittest

from Module13.classes.number_guesser import NumberGuesser


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.number_guesser = NumberGuesser()

    def tearDown(self):
        del self.number_guesser

    def test_add_guess(self):
        self.number_guesser.add_guess(1)
        self.assertEqual(self.number_guesser.guessed_list[0], 1)


if __name__ == '__main__':
    unittest.main()
