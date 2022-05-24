class Account:
    pass

    def __init__(self, name):
        self.balance = 0
        self.name = name

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")

        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("You can not deposit negative amount")


        elif amount > self.balance:
            raise ValueError("Withdrawal can not be more than deposit")



        self.balance -= amount


    def tranfer(self,amount):
        pass



