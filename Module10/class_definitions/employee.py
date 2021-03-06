"""
Program: employee.py
Author: Paul Ford
Last date modified: 07/1/2020
Purpose: Create my first class
"""
from datetime import datetime


class Employee:
    """Employee Class """

    # Constructor
    def __init__(self, lname, fname, add, pnumber,):
        self._last_name = lname
        self._first_name = fname
        self._address = add
        self._phone_number = pnumber

    def __str__(self):
        """
        unformatted version of Employee data
        :return: str of employee data
        """
        return "Employee attributes {}, {}, {} ,{},". \
            format(self._last_name, self._first_name, self._address, self._phone_number)

    def __repr__(self):
        """
        friendly formatted of Employee Data
        :return: str of formatted employee data.
        """

        return str(self._first_name) + " " + str(self._last_name) + "\n" + \
            str(self._address) + " \n"

    def display(self):
        """
        displays attributes of classes
        :return: a string with attributes.
        """
        return self.__repr__()



# Driver
#date = datetime(2020, 1, 15)  # create a datetime to confirm
# call the constructor, needs to have a first and last name in parameter
#emp = Employee('Ruiz', 'Matthew', '4045 Aspen Hills Dr. \nAustin, TX', '563-650-2859', False, date,
#               '10.00')  # call the constructor, needs to have a first and last name in parameter
#emp1 = Employee('Ford', 'Paul', '4045 Aspen Hills Dr. \nAustin, TX', '563-650-2859', True, date,
#                '50,000')

#print(emp.display())  # display returns a str, so print the information
#(emp1.display())
# emp  # clean up!
#del emp1
