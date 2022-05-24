class bankaccount:
    def __init__(self):
        self.balance = 0
        print("Hello1 Welcome to the deposit and withdrawal machine")

    def deposit(self):
        amount = float(input("Enter amount you want to deposit: "))
        self.balance += amount
        print("\n You deposit:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n Amount withdraw is:", amount)

        else:
            print("\n Insufficient balance  ")

    def display(self):
        print("\n Available balance is =", self.balance)

s = bankaccount()


s.deposit()
s.withdraw()
s.display()


















