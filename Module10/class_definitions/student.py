from datetime import datetime


class Student:
    """Student class"""

    def __init__(self, lname, fname, major, startdate, gpa=''):
        """
        constructor to create a student
        :param lname: last name
        :param fname: first name
        :param major: Major of student
        :param gpa: students gpa on a 4.0 scale
        """
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-' '")
        '''
        Checking values for good input
        '''
        if not (name_characters.issuperset(lname)):
            raise ValueError
        if not (name_characters.issuperset(fname)):
            raise ValueError
        if not (name_characters.issuperset(major)):
            raise ValueError
        if not isinstance(gpa, float):
            raise ValueError
        if not 0 <= gpa <= 4:
            raise ValueError

        '''
        Setting constructor values
        '''
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self._start_date = startdate
        self.gpa = gpa

    def __str__(self):
        """
        prints student data
        :return: str of students data
        """
        return self.last_name + ", " + self.first_name + " has major " + self.major + \
            "\nStart Date: " + str(self._start_date) + \
            '\nGPA: ' + str(self.gpa)

    def change_major(self, new_major):
        """
        changes the major of the student
        checks if the new major is valid
        :param new_major: new major to change.
        """
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!'- ' '")
        if not (name_characters.issuperset(new_major)):
            raise ValueError
        self.major = new_major

    def update_gpa(self, new_gpa):
        """
        updates the gpa of the student
        :param new_gpa: new GPA
        """
        if not isinstance(new_gpa, float):
            raise ValueError
        if not 0 <= new_gpa <= 4:
            raise ValueError
        self.gpa = new_gpa

    def display(self):
        """
        A better formatted version of student data
        :return: str of student data
        """
        return "First Name: " + self.first_name + "\nLast Name:  " + self.last_name + \
            "\nMajor: " + self.major + \
            "\nStart Date: " + str(self._start_date) + \
            '\nGPA: ' + str(self.gpa)

# driver
# start_date = datetime(2018, 9, 1)  # create a datetime to confirm
# student = Student('Ford', 'Paul', 'English', start_date, 4.0)
# print(student)
