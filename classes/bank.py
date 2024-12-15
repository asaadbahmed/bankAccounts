class bank:
    REGISTERED_BANKS = set()
    
    def __init__(self, name, maxAccounts, minimumAgeRequirement = 18):
        if name in bank.REGISTERED_BANKS:
            raise Exception(f"There is already a bank registered with the name {name}, choose a different name.")
        
        bank.REGISTERED_BANKS.add(name)
        self.minimumAgeRequirement = minimumAgeRequirement
        self.name = name
        self.accounts = []
        self.maxAccounts = maxAccounts

    def __str__(self):
        return f"Bank Name: {self.name}\t\tAccounts: {len(self.accounts)} / {self.maxAccounts}\t\tMinimum Age Requirement: {self.minimumAgeRequirement}"
    
    def registerAccount(self, account):
        for account in self.accounts:
            if account.number == account.number or account.age < self.minimumAgeRequirement:
                return False

        self.accounts.append(account)        
        return True

    def getAgeRequirement(self):
        return self.minimumAgeRequirement

    def getName(self):
        return self.name
    
    def getNumAccounts(self):
        return len(self.accounts)
    
    def getAccounts(self):
        return self.accounts