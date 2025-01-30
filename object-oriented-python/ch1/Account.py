class Account:
    def __init__(self, name, balance, password):
        self.name = name
        self.password = int(password)
        self.balance = balance

    def show(self):
        print(f"       Name: {self.name}")
        print(f"       Balance: {self.balance}")
        print(f"       Password: {self.password}")
        print()

    def get_balance(self, password):
        if password == self.password:
            return self.balance
        else:
            print("Incorrect password")
            return None

    def deposit(self, amount_to_deposit, password):
        if self.password != password:
            print("Incorrect password")
            return None
        if amount_to_deposit < 1:
            print("You must deposit some amount")
            return None
        self.balance = self.balance + amount_to_deposit
        return self.balance

    def withdraw(self, amount_to_withdraw, password):
        if password != self.password:
            print("Incorrect password")
            return None
        if amount_to_withdraw < 1:
            print("You cannot withdraw negative or zero amount ")
            return None
        if amount_to_withdraw > self.balance:
            print("You cannot withdraw more than you have in your account")
            return None
        self.balance = self.balance - amount_to_withdraw
        return self.balance
