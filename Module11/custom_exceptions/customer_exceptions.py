"""
Program: customer.py
Author: Paul Ford
Last date modified: 07/1/2020
Purpose: Create my first class
"""


class Customer:
    """Customer Class"""

    # Constructor
    def __init__(self, cust_id, lname, fname, pnumber):
        # check to see if first and last name is alpha characters, if not throw exception
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!'- ' '")
        if not (name_characters.issuperset(str(lname))):
            raise InvalidNameException
        if not (name_characters.issuperset(str(fname))):
            raise InvalidNameException
        # first check to see if number is 12 digits long
        if len(pnumber) != 12:
            raise InvalidPhoneNumberFormat
        # now check for the dashes in the right spot
        for i in range(12):
            if i in [3, 7]:
                if pnumber[i] != '-':
                    raise InvalidPhoneNumberFormat
                # last verify all the values are numbers
            elif not pnumber[i].isalnum():
                raise InvalidPhoneNumberFormat
        # check to see if its an int
        if not isinstance(cust_id, int):
            raise InvalidCustomerIdException
        # check range
        if cust_id < 1000 or cust_id > 9999:
            raise InvalidCustomerIdException
        # setting attributes
        self._customer_id = cust_id
        self._last_name = lname
        self._first_name = fname
        self._phone_number = pnumber

    def __str__(self):
        """
        dispalys objects
        :return: un formatted str
        """
        return str(self._customer_id) + ", " + \
            self._last_name + ", " + self._first_name + ", " + \
            self._phone_number

    def __repr__(self):
        """
        format the string object
        :return: formatted version of object
        """
        return "Customer ID: " + str(self._customer_id) + '\n' \
            "Name: " + self._last_name + " " + self._first_name + '\n' \
            "Phone: " + self._phone_number + '\n' \


 # Methods
    def display(self):
        """
        confirms that custID is a number and displays the object attrubutes
        :return: formatted string of the attributes
        """
        if isinstance(self._customer_id, int):
            return self.__repr__()
        else:
            raise AttributeError("'Customer' object has no attribute  'cid'")


class InvalidCustomerIdException(Exception):
    pass


class InvalidNameException(Exception):
    pass


class InvalidPhoneNumberFormat(Exception):
    pass


# Drivers
try:
    cust = Customer(99, 'Paul', 'Ford', '123-123-1234')
except InvalidCustomerIdException:
    print('The customerID is incorrect.')

try:
    cust = Customer(99, 3434, 'Ford', '123-123-1234')
except InvalidNameException:
    print('First name is incorrect')

try:
    cust = Customer(99, 'Paul', 41234, '123-123-1234')
except InvalidNameException:
    print('Last name is incorrect')

try:
    cust = Customer(99, 'Paul', 'Ford', '123-123-124')
except InvalidPhoneNumberFormat:
    print('Phone number is in the wrong format')
