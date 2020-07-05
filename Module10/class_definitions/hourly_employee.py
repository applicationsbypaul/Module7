"""
Program: hourly_employee.py
Author: Paul Ford
Last date modified: 07/1/2020
Purpose: hourly employee
"""
from datetime import datetime

from Module10.class_definitions.employee import Employee


class HourlyEmployee(Employee):
    def __init__(self, lname, fname, add, pnumber, startdate, salary):
        super().__init__(lname, fname, add, pnumber)
        self._start_date = startdate
        self._salary = salary

    def __str__(self):
        """
        unformatted version of Employee data
        :return: str of employee data
        """
        return "Employee attributes {}, {}, {} ,{}, {}, {}". \
            format(self._last_name, self._first_name, self._address, self._phone_number,
                   self._start_date, self._salary)

    def give_raise(self, new_salary):
        self._salary = new_salary

    def display(self):
        return super().display() + 'Start Date: ' + \
               str(self._start_date) + '\nSalary: $' + self._salary + \
               '\hour'


# Driver
date = datetime(2020, 1, 15)  # create a datetime to confirm
# call the constructor, needs to have a first and last name in parameter
emp = HourlyEmployee('Ruiz', 'Matthew', '4045 Aspen Hills Dr. \nAustin, TX',
                       '563-650-2859', date, '10.00')
print(emp.display())
emp.give_raise('12,000')
print(emp.display())
# cleaning up memory
del date, emp
