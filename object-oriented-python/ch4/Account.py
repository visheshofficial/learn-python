class Account:
    """A class account to represent a simple bank account"""

    def __init__(self, name: str, balance: float, password: str) -> None:
        """Initialize the account with provided name, balance and password

        Args:
            name: The account holder's name
            balance: The initial balance of the account
            password: The password for accessing the account

        """
        self._name = name
        self._balance = int(balance)
        self._password = password

    def display_info(self) -> None:
        """Print the account's name, balance and password"""
        print(f"Name:{self._name}")
        print(f"Balance:{self._balance}")
        print(f"PAssword:{self._password}")
        print()

    def get_balance(self, password: str) -> float | None:
        """Return the account balance if the provided password matches the account's password.
        Print an error message and return None otherwise.

        Args:
            password (str): The Password to access account balance

        Returns:
            The balance if the password is correct; otherwise None
        """
        if self._password == password:
            return self._balance
        else:
            print("Incorrect password")
            return None

    def deposit(self, amount: float, password: str) -> float | None:
        """Deposit the specified amount into the account if the password is correct
        and the amount is positive.

        Args:
            password (str): The password to validate
            amount (float): The amount to deposit

        Returns:
            The new balance if the deposit is succesful; otherwise None
        """
        if password != self._password:
            print("Incorrect password.")
            return None

        if amount < 1:
            print("You must deposit a positive amount.")
            return None

        self._balance += amount
        return self._balance

    def withdraw(self, amount: float, password: str) -> float | None:
        """Withdraw the specific amount fromn the balance if the password is correct,
        and the amount is poasitive and there is sufficient balance, otherwise None

        Args:
            amount (float): The amount to be withdraw
            password (str): The password to validate

        Returns:
            The new blalance after the withdraw if succesful; otherwise None_
        """
        if password != self._password:
            print("Incorrect password.")
            return None

        if amount > self._balance:
            print("Insufficient balance.")
            return None

        if amount < 1:
            print("Can withdraw only positive amount.")
            return None

        self._balance -= amount
        return self._balance
