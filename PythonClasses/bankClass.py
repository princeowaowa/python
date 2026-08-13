class Bank:
    # Constructor to initialize the bank account with a name and balance
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

        # API for depositing money into the bank account --> database upate
        return f"Deposited {amount}. New balance is {self.balance}."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        return f"Withdrew {amount}. New balance is {self.balance}."

    def get_balance(self):
        return f"Current balance is {self.balance}."



bank_account = Bank("John Doe", 1000)
bank_account.deposit(500)
bank_account.deposit(500)
bank_account.deposit(500)

bank_account.withdraw(2000)


print(bank_account.get_balance())  # Output: Current balance is 2500.