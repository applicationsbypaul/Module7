"""
Program: Person.py
Author: Paul Ford
Last date modified: 07/5/2020
Purpose: Create a class that uses another object in creation.
"""
from datetime import datetime

from Module10.class_definitions.student import Student


class Person:
    """Person class"""

    def __init__(self, student, addy=''):
        """
        Constructor to create
        :param student: student
        :param addy: address
        """
        self.address = addy
        self.student = student

    def __str__(self):
        """
        prints person data
        :return: str of person data
        """
        return student.display() + '\nAddress: ' + self.address


# Driver
start_date = datetime(2018, 9, 1)  # create a datetime to confirm
student = Student('Ford', 'Paul', 'English', start_date, 4.0)
paul = Person(student, '1234 Chicago LN, Chicago, IL')
print(paul)
paul.student.change_major('BeingAwesome!')
paul.student.update_gpa(3.0)
print(paul)
# clean up object
del paul
