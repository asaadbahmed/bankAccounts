import unittest
from account import account

class accountTests(unittest.TestCase):
    def test_valid_deposit(self):
        a = account("John Doe", 100)
        self.assertTrue(a.deposit(50))
        self.assertEqual(a.getBalance(), 150)
    
    def test_invalid_deposit(self):
        a = account("John Doe", 100)
        self.assertFalse(a.deposit(-50))
        self.assertEqual(a.getBalance(), 100)

    def test_valid_withdraw(self):
        a = account("John Doe", 100)
        self.assertTrue(a.withdraw(50))
        self.assertEqual(a.getBalance(), 50)

    def test_invalid_withdraw(self):
        a = account("John Doe", 100)
        self.assertFalse(a.withdraw(-50))
        self.assertEqual(a.getBalance(), 100)
    
unittest.main()