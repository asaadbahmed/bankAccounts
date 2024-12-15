import unittest
from account import account
from bank import bank

class TestAccount(unittest.TestCase):
    def test_account_creation(self):
        acc = account("Asaad Ahmed", 10000)
        self.assertEqual(acc.name, "Asaad Ahmed")
        self.assertEqual(acc.balance, 10000)

    def test_deposit(self):
        acc = account("Asaad Ahmed", 10000)
        acc.deposit(500)
        self.assertEqual(acc.balance, 10500)

    def test_withdraw(self):
        acc = account("Asaad Ahmed", 10000)
        acc.withdraw(500)
        self.assertEqual(acc.balance, 9500)

class TestBank(unittest.TestCase):
    def test_bank_creation(self):
        bnk = bank("Royal Bank of Canada", 100)
        self.assertEqual(bnk.name, "Royal Bank of Canada")

unittest.main()