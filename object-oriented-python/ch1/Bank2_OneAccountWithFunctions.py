# No OOP
# Bank Version 1
# Single Account

account_name = ""
account_balance = 0
account_password = ""


def new_account(name, balance, password):
    global account_balance, account_name, account_password
    account_name = name
    account_balance = balance
    account_password = password


def show():
    global account_balance, account_name, account_password
    print(f"       Name: {account_name}")
    print(f"       Balance: {account_balance}")
    print(f"       Password: {account_password}")
    print()


def get_balance(password):
    global account_balance, account_name, account_password
    if password == account_password:
        return account_balance
    else:
        print("Incorrect password")
        return None


def deposit(amount_to_deposit, password):
    global account_balance, account_name, account_password
    if user_password != account_password:
        print("Incorrect password")
        return None
    if user_deposit_amount < 1:
        print("You must deposit some amount")
        return None
    account_balance = account_balance + user_deposit_amount
    return account_balance


def withdraw(amount_to_withdraw, password):
    global account_balance, account_name, account_password
    if password != account_password:
        print("Incorrect password")
        return None
    if amount_to_withdraw < 1:
        print("You cannot withdraw negative or zero amount ")
        return None
    if amount_to_withdraw > account_balance:
        print("You cannot withdraw more than you have in your account")
        return None
    account_balance = account_balance - amount_to_withdraw
    return account_balance


new_account("Joe", 100, "soup")  # create an account


while True:
    print()
    print("Press b to show balance")
    print("Press w to make a withdrawal")
    print("Press d to make a deposit")
    print("Press s to show the account")
    print()

    action = input("What do you want to do ?")
    action = action.lower()
    action = action[0]
    print()

    if action == "b":
        print("Get balance:")
        user_password = input("Please enter the password:")
        current_balance = get_balance(user_password)
        if current_balance is not None:
            print(f"Your balance is {current_balance}")

    elif action == "d":
        print("Deposit:")
        user_deposit_amount = input("Please enter amount to deposit: ")
        user_deposit_amount = int(user_deposit_amount)
        user_password = input("Please enter the password")
        new_balance = deposit(user_deposit_amount, user_password)
        if new_balance is not None:
            print("Your new balance is:", new_balance)

    elif action == "s":
        print("Show Account:")
        show()

    elif action == "w":
        print("Withdraw:")
        user_withdraw_amount = input("Please enter amount to withdraw: ")
        user_withdraw_amount = int(user_withdraw_amount)
        user_password = input("Please enter the password")
        new_balance = withdraw(user_withdraw_amount, user_password)
        if new_balance is not None:
            print("Your new balance is:", new_balance)

    elif action == "q":
        break

print("Done")
