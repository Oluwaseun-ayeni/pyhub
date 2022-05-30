class Account(object):

    def __init__(self, owner, balance):
        self.balance = balance
        self.owner = owner

    def withdraw(self, amount):
        if amount < self.balance:
            return 'Withdrawal successful'

        elif amount > self.balance:
            return 'Funds unavailable'


        else:
            raise ValueError('Withdrawal failed')

    def deposit(self, amount):
        self.balance = amount + self.balance
        if amount > 0:
            return 'Deposit accepted'

        else:
            raise ValueError('Can not make negative deposit')

    def __str__(self):
        return f"Owner: {self.owner} \nBalance: {self.balance}"


acct1 = Account('Storm', 100)
print(acct1.withdraw(200))
print(acct1.deposit(23))
print(acct1)
