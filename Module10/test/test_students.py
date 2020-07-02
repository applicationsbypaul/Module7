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

    def test_inital_all_attributes(self):
        student = Student('Ford', 'Paul', 'Computer Engineering', 3.5)  # this is not self.person from setUp, but local
        assert student.last_name == 'Ford'                               # note no self here on person or assert
        assert student.first_name == 'Paul'
        assert student.major == 'Computer Engineering'
        assert student.gpa == 3.5



if __name__ == '__main__':
    unittest.main()
