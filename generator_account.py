class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

    def __str__(self):
        return f"Insufficient balance {self.balance} for withdraw amount {self.amount}"


class Account:
    minbal = 5000

    @staticmethod
    def getminbal():
        return Account.minbal

    # Constructor
    def __init__(self, acno, customer, balance=0):
        # Object attributes or Fields or Instance Variables
        self.acno = acno
        self.customer = customer
        self.balance = balance

    # Methods
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - Account.minbal >= amount:
            self.balance -= amount
        else:
            raise InsufficientFundsError(self.balance, amount)

    def getbalance(self):
        return self.balance


a1 = Account(1, "Marshall")
a1.deposit(10000)
a1.deposit(20000)
try:
    a1.withdraw(50000)
    print(a1.getbalance())
except InsufficientFundsError as ex:
    print(ex)

a2 = Account(2, "Tom", 5000)
a2.deposit(50000)
print(a2.getbalance())