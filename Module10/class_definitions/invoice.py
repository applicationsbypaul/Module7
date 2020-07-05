"""
Program: invoice.py
Author: Paul Ford
Last date modified: 07/1/2020
Purpose: Create invoice class with atr.
"""
from Module10.class_definitions.customer import Customer


class Invoice:
    """Invoice Class"""

    # Constructor
    def __init__(self, invID, customer, items={}):
        self.customer = customer
        self._invoice_id = invID
        self._items_with_price = items

    def __str__(self):
        """
        unformatted Invoice data
        :return: invoice data information.
        """
        return 'Invoice Attributes: {}, {}, {}, {}, {}, {}' \
            .format(self._invoice_id, self.customer._customer_id,
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
        tax = .07  # tax for calculation
        total = 0  # var for total tax
        print(repr(self.customer))
        for item in self._items_with_price:
            print(item + '.....$' + str(self._items_with_price[item]))
            total = self._items_with_price[item] + total
        tax = round(total * tax, 2)
        total = tax + total

        print('Tax........' + "${:,.2f}".format(tax))
        print('Total...... ' + "${:,.2f}".format(total))


# Driver code
captain_mal = Customer(1, 'Reynolds', 'Mel', 'No phones', 'Firefly, somewhere in the verse')
invoice = Invoice(1, captain_mal)
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()
