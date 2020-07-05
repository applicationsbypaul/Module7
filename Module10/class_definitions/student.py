class Student:
    """Student class"""

    def __init__(self, lname, fname, major, gpa=0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-' '")
        if not (name_characters.issuperset(lname)):
            raise ValueError
        if not (name_characters.issuperset(fname)):
            raise ValueError
        if not (name_characters.issuperset(major)):
            raise ValueError
        if not isinstance(gpa, float) or not (0 > gpa > 4):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major


    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + "with gpa: " + str(self.gpa)


# driver
s = Student('Ford', 'Paul', 'English', 4.5)
