import unittest
from classes.account import account
from classes.bank import bank

# otherwise the tests will run in alphabetical order, causing the test_bank_register_duplicate to run first
unittest.TestLoader.sortTestMethodsUsing = None

class bankTests(unittest.TestCase):
    def test_bank_register(self):
        b = bank("Royal Bank of Canada", 10)
        self.assertEqual(b.getName(), "Royal Bank of Canada")
        self.assertEqual(b.getNumAccounts(), 0)
        self.assertEqual(b.getAccounts(), [])

    def test_bank_register_duplicate(self):
        self.assertRaises(Exception, bank, "Royal Bank of Canada", 10)

    def test_bank_register_account(self):
        b = bank("Toronto Dominion Bank", 10)
        acc = account("Jane Doe", 100)
        self.assertTrue(b.registerAccount(acc))
        self.assertEqual(b.getNumAccounts(), 1)
        self.assertEqual(b.getAccounts(), [acc])

if __name__ == "__main__":
    unittest.main()