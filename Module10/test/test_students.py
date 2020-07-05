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

    def test_initial_all_attributes(self):
        student = Student('Ford', 'Paul', 'Computer Engineering', 3.5)  # this is not self.person from setUp, but local
        assert student.last_name == 'Ford'  # note no self here on person or assert
        assert student.first_name == 'Paul'
        assert student.major == 'Computer Engineering'
        assert student.gpa == 3.5

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            s = Student('123', 'Paul', 'English')

    def test_object_not_created_error_fist_name(self):
        with self.assertRaises(ValueError):
            s = Student('Ford', '123', 'English')

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            a = Student('Ford', 'Paul', '234')

    def test_object_not_created_error_gpa(self):
        with self.asserRaises(ValueError):
            s = Student('Ford', 'Paul', 'Eng', 4.5)


if __name__ == '__main__':
    unittest.main()
