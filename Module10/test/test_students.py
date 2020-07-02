import unittest

from Module10.class_definitions.student import Student


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = Student('Ford', 'Paul', 'Computer Engineering')

    def tearDown(self):
        del self.student

    def test_initial_value_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Ford')
        self.assertEqual(self.student.first_name, 'Paul')
        self.assertEqual(self.student.major, 'Computer Engineering')


if __name__ == '__main__':
    unittest.main()
