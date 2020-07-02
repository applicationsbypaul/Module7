"""
Program: invoice.py
Author: Paul Ford
Last date modified: 07/1/2020
Purpose: Create invoice class with atr.
"""


class Invoice:
    """Invoice Class"""

    # Constructor
    def __init__(self, invID, custID, lname, fname, phone, addy, items={}):
        self._invoice_id = invID
        self._customer_id = custID
        self._last_name = lname
        self._first_name = fname
        self._phone_number = phone
        self._address = addy
        self._items_with_price = items

    def __str__(self):
        """
        unformatted Invoice data
        :return: invoice data information.
        """
        return 'Invoice Attributes: {}, {}, {}, {}, {}, {}' \
            .format(self._invoice_id, self._customer_id,
                    self._last_name, self._first_name, self._phone_number,
                    self._address)

    def __repr__(self):
        """
        print the items with the price
        :return: str value of items
        """
        return print(self._items_with_price)

    def add_item(self, item):
        """
        Adds an item to the item list
        :param item:  an item and price
        """
        self._items_with_price.update(item)

    def create_invoice(self):
        """
        Calculates the total and tax and prints out
        the invoice
        :return:
        """
        tax = .07       # tax for calculation
        total = 0       # var for total tax
        for item in self._items_with_price:
            print(item + '.....$' + str(self._items_with_price[item]))
            total = self._items_with_price[item] + total
        tax = round(total * tax, 2)
        total = tax + total
        print('Tax........' + "${:,.2f}". format(tax))
        print('Total...... ' + "${:,.2f}". format(total))


# Driver code
invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802', 'Mouse', 'Minnie', '555-867-5309')
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()
