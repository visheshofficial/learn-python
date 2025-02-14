from account import *

accounts = {}
next_account_number = 0

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
