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
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!'- ' '")
        if not (name_characters.issuperset(lname)):
            raise InvalidNameException
        if not (name_characters.issuperset(fname)):
            raise InvalidNameException
        if len(pnumber) != 12:
            raise InvalidPhoneNumberFormat
        for i in range(12):
            if i in [3, 7]:
                if pnumber[i] != '-':
                    raise InvalidPhoneNumberFormat
            elif not pnumber[i].isalnum():
                raise InvalidPhoneNumberFormat

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
 \
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


# Driver
"""

# call the constructor, needs to have a first and last name in parameter
customer1 = Customer(4704345, 'Ford', 'Paul', '713-459-1234', '4045 Aspen Hills Dr. \nAustin, TX')
print(customer1.display())
customer2 = Customer('470422', 'Miller', 'Trevor', '555-555-5555', '1234 Chicago Ave. \nChicago, IL')
print(customer2.display())
# cleaning up
del customer1
del customer2

"""
