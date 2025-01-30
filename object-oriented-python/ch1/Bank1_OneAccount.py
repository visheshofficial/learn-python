# No OOP
# Bank Version 1
# Single Account

account_name = "Joe"
account_balance = 100
account_password = "soup"

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
        if user_password == account_password:
            print(f"Your balance is {account_balance}")
        else:
            print("Incorrect password")
    elif action == "d":
        print("Deposit:")
        user_deposit_amount = input("Please enter amount to deposit: ")
        user_deposit_amount = int(user_deposit_amount)
        user_password = input("Please enter the password")
        if user_password != account_password:
            print("Incorrect password")
        elif user_deposit_amount < 1:
            print("You must deposit some amount")
        else:
            account_balance = account_balance + user_deposit_amount
            print(f"Your new balance is: {account_balance}")

    elif action == "s":
        print("Show Account:")
        print(f"       Name: {account_name}")
        print(f"       Balance: {account_balance}")
        print(f"       Password: {account_password}")
        print()
    elif action == "w":
        print("Withdraw:")
        user_withdraw_amount = input("Please enter amount to withdraw: ")
        user_withdraw_amount = int(user_withdraw_amount)
        user_password = input("Please enter the password")
        if user_password != account_password:
            print("Incorrect password")
        elif user_withdraw_amount < 1:
            print("You cannot withdraw negative or zero amount ")
        elif user_withdraw_amount > account_balance:
            print("You cannot withdraw more than you have in your account")
        else:
            account_balance = account_balance - user_withdraw_amount
            print(f"Your new balance is: {account_balance}")
    elif action == "q":
        break

print("Done")
