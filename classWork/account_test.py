import unittest

from . import account


class AccountTest(unittest.TestCase):
    def test_that_account_can_be_created(self):
        account1 = account.Account("Storm")

        self.assertIsNotNone(account1)
        self.assertIsInstance(account1, account.Account)

    def test_that_account_has_a_name(self):
        """"
        GIVEN:
        WHEN:
        THEN:

        """
        account1 = account.Account("Storm")
        name = account1.name
        self.assertEqual("Storm", name)

    def test_that_account_can_depoist(self):
        """"
        GIVEN:
        WHEN:when a deposit is made
        THEN:account balance should reflect

        """
        account1 = account.Account("Storm")
        account1.deposit = 2000

        self.assertEqual(2000, account1.balance)

    def test_that_negative_deposit_raises_error(self):
        account1 = account.Account("Storm")

        account1.deposit(500)

        self.assertRaises(ValueError, account1.deposit, -1000)

        self.assertEqual(500, account1.balance)



    def test_that_account_can_withdraw(self):
        account1 =account.Account("Storm")

        account1.withdraw(300)

        self.assertRaises(ValueError,account1.withdraw, -300)

        self.assertRaises(ValueError,account1.withdraw, 200)

        self.assertEqual(200, account1.balance)



    def test_that_account_can_transfer(self):
         account1 = account.Account("Storm")
















if __name__ == '__main__':
    unittest.main()
