class bank:
    registered_banks = set()

    def __init__(self, name, maxAccounts):
        if name in bank.registered_banks:
            raise Exception(f"There is already a bank registered with the name {name}, choose a different name.")
        
        bank.registered_banks.add(name)
        self.name = name
        self.accounts = []
        self.maxAccounts = maxAccounts

    def __str__(self):
        return f"Bank Name: {self.name}\t\tAccounts: {len(self.accounts)} / {self.maxAccounts}"
    
    def registerAccount(self, account):
        for account in self.accounts:
            if account.number == account.number:
                return False

        self.accounts.append(account)        
        return True

    def getName(self):
        return self.name
    
    def getNumAccounts(self):
        return len(self.accounts)
    
    def getAccounts(self):
        return self.accounts