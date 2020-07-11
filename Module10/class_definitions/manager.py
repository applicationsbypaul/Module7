"""
Program: manager.py
Author: Paul Ford
Last date modified: 07/1/2020
Purpose: Create my first class
"""
from datetime import datetime

from Module10.class_definitions.employee import Employee
from Module10.class_definitions.persons import Persons
from Module10.class_definitions.salaried_employee import SalariedEmployee


class Manager(Employee, Persons):
    """Manager class"""

    def __init__(self, dep, emp_list, lname, fname, add, pnumber, salaried, startdate, salary):
        super().__init__(lname, fname, add, pnumber, salaried, startdate, salary,)
        self.department = dep
        self.direct_reports = emp_list

    def display(self):
        employee_list = ''
        for employee in self.direct_reports:
            employee_list = '(' + employee._first_name + ',' + employee._last_name + ')' + \
                            employee_list
        return Employee.display(self) + '\nDepartment: ' + self.department + \
            '\nEmployees: ' + employee_list


# driver
# creating a couple of employees
date = datetime(2020, 1, 15)  # create a datetime to confirm
date2 = datetime(2020, 3, 15)  # create a datetime to confirm
emp = Employee('Ruiz', 'Matthew', '4045 Aspen Hills Dr. \nAustin, TX', '563-650-2859', False, date,
               '10.00')  # call the constructor, needs to have a first and last name in parameter
emp1 = Employee('Ford', 'Paul', '4045 Aspen Hills Dr. \nAustin, TX', '563-650-2859', True, date2,
                '50,000')
Trevor = Manager('IT', [emp, emp1], 'Miller', 'Trevor', '1234 Chicago LN Chicago, IL',
                 '555-123-4567', True, date2, '40,000')
print(Trevor.display())
# prints the display i created in manager
Trevor.update_salary('42000')
print(Trevor.display())

# clean up memory
del date, date2, emp, emp1, Trevor
