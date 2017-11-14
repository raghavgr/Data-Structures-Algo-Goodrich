class CreditCard:
    """A consumer credit card"""

    def __init__(self, customer, bank, account, limit):
        """Create a new credit card instance.

        The initial balance is zero.

        :param customer: the name of customer
        :param bank:     the name of bank
        :param account:     the account identifier
        :param limit:    credit limit(in $)
        """

        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return name of bank."""
        return self._bank

    def get_account(self):
        """Return the card identifying number (a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance

    # 2.30
    def set_balance(self, new_balance):
        self._balance = new_balance
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed. False if charge was denied.
        """
        if price + self._balance > self._limit:     # if charge exceeds limit
            return False                            # deny charge
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount

# cc = CreditCard( 'John Doe',   '1st Bank' ,   '5391 0375 9387 5309' , 1000)
# print(cc.get_account())
# print(cc.get_balance())
# cc.charge(900)
# print(cc.get_balance())