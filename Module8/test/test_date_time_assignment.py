import unittest
import datetime

from Module8.more_fun_with_collections.date_time_assignment import half_birthday

recent_birthday = datetime.datetime(2020, 5, 21)


class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        self.assertEqual(half_birthday(recent_birthday), datetime.datetime(2020, 11, 19))


if __name__ == '__main__':
    unittest.main()
