"""
Program: students.py
Author: Paul Ford
Last date modified: 07/1/2020
Purpose: Implementing inheritance
"""
from Module10.class_definitions.persons import Persons


class Students(Persons):
    """Students class"""

    def __init__(self, studentID, lname, fname, major='Computer Science', gpa=0.0, ):
        """
        constructor to create a student
        :param studentID: students ID number
        :param lname: last name
        :param fname: first name
        :param major: Major of student
        :param gpa: students gpa on a 4.0 scale
        """
        super().__init__(lname, fname)
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-' '")
        '''
        Checking values for good input
        '''
        if not (name_characters.issuperset(major)):
            raise ValueError
        if not isinstance(gpa, float):
            raise ValueError
        if not 0 <= gpa <= 4:
            raise ValueError
        if not isinstance(studentID, int):
            raise ValueError

        '''
        Setting constructor values
        '''
        self._student_id = studentID
        self._major = major
        self._gpa = gpa

    def display(self):
        display = self._last_name + ', ' + self._first_name + ':(' + str(self._student_id) + \
                  ') ' + self._major + ' gpa: ' + str(self._gpa)
        return display


# driver
my_student = Students(900111111, 'Song', 'River')
print(my_student.display())
my_student = Students(900111111, 'Song', 'River', 'Computer Engineering')
print(my_student.display())
my_student = Students(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
print(my_student.display())
del my_student
