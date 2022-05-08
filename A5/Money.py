class Money:
    """
    A class for manipulation of different currencies

    class attributes:
        conversion_rate (float)
    instance attributes:
        amount (float)
        currency (str)
    class methods:
        set_conversion_rate: resets conversion rate
        __add__: implements addition of monies (right side currency converted to left side if different)
        __sub__: implements subtraction of monies
    """
    # YOUR CODE HERE
    conversion_rate = 10.0

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def set_conversion_rate(self, new_conversion_rate):
        self.conversion_rate = new_conversion_rate

    def __add__(self, other):
        if self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        else:
            return Money(self.amount + other.amount * self.conversion_rate, self.currency)

    def __sub__(self, other):
        if self.currency == other.currency:
            return Money(self.amount - other.amount, self.currency)
        else:
            return Money(self.amount - other.amount / self.conversion_rate, self.currency)
    ################

ma = Money(10, "USD")
ma.set_conversion_rate(20)
print(ma.conversion_rate)