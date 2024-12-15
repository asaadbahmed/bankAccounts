class account:
    TOTAL_ACCOUNTS = 0

    """
    "name" refers to first and last name of the person opening the account
    "number" refers to the account number, this is a unique identifier
    """
    def __init__(self, name, age, initialBalance = 0.0):
        account.TOTAL_ACCOUNTS += 1
        self.age = age
        self.name = name
        self.number = account.TOTAL_ACCOUNTS
        self.balance = initialBalance

    def __str__(self):
        return f"Account Name: {self.name}\tAccount Number: {self.number}\tAccount Balance: ${self.balance:,.2f}"
       
    def getAccountName(self):
        return self.name

    def getBalance(self):
        return f"${self.balance:,.2f}"
    
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