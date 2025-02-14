from account import Account  # Module names should be lowercase (PEP 8)

# Create accounts and store them in a list
accounts: list[Account] = [
    Account("Joe", 100, "JoesPassword"),
    Account("Mary", 12345, "MarysPassword"),
]

for account in accounts:
    account.display_info()
