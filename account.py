class account:
    totalAccounts = 0

    """
    "name" refers to first and last name of the person opening the account
    "number" refers to the account number, this is a unique identifier
    """
    def __init__(self, name, initialBalance = 0):
        account.totalAccounts += 1
        self.name = name
        self.number = account.totalAccounts
        self.balance = initialBalance

    def __str__(self):
        return f"Account Name: {self.name}\tAccount Number: {self.number}\tAccount Balance: ${self.balance:,.2f}"
       
    def getAccountName(self):
        return self.name

    def getBalance(self):
        return self.balance
    
    def getAccountNumber(self):
        return self.number
    
    def deposit(self, amount):
        if amount <= 0: return False
        self.balance += amount
        return True
    
    def withdraw(self, amount):
        if amount > self.balance or amount <= 0: return False
        self.balance -= amount
        return True