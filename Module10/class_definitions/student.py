class Student:
    """Student class"""

    def __init__(self, lname, fname, major, gpa=''):
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
        self.gpa = gpa

    def __str__(self):
        """
        prints student data
        :return: str of students data
        """
        return self.last_name + ", " + self.first_name + " has major " + self.major + "with gpa: " + str(self.gpa)
