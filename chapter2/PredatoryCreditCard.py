from chapter2 import CreditCard


class PredatoryCreditCard(CreditCard.CreditCard):
    """An extension to CreditCard that compounds interest adn fees"""

    def __init__(self, customer, bank, account, limit, apr):
        """
        Create a new PredatoryCreditCard instance.

        Initial balance is zero.

        :param customer:the name of customer
        :param bank:    the name of bank
        :param account: the account identifier
        :param limit:   credit limit(in $)
        :param apr:     annual percentage rate (e.g., 0.0825 or 8.25% APR)
        """

        super().__init__(customer, bank, account, limit)
        self._apr = apr

    def charge(self, price):
        """Charge given price to the card, assuming sufficient card limit.

        Return True if charge was processed.
        Return False and add $5 fee if charge is denied.
        """
        print(price,"is being charged")
        success = super().charge(price)        # call inherited method
        if not success:
            self._balance += 5          # add fee
        return success                  # return True or False

    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
            # if balance is positive, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor


pcc = PredatoryCreditCard('John Doe',   '1st Bank' ,   '5391 0375 9387 5309' , 1000, 0.05)
print(pcc.get_balance())
pcc.charge(2000)
print(pcc.get_balance())