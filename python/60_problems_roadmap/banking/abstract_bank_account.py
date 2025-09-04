from abc import ABC, abstractmethod


# AbstractBankAccount is an abstract base class that defines what bank accounts should be able to do — without saying how they do it.
# Then, BankAccount class will implement those abstract methods.
class AbstractBankAccount(ABC):

    @property
    @abstractmethod
    def balance(self):
        """Getting the current account balance."""
        pass

    @property
    @abstractmethod
    def email(self):
        """Getting email of the account holder."""
        pass

    @email.setter
    @abstractmethod
    def email(self, new_email):
        """Setting email of the account holder."""
        pass

    @abstractmethod
    def deposit(self, amount):
        """
        Deposit a given amount into the account.

        Args:
            amount (float): Amount to deposit, must be greater than 0.

        Raises:
            ValueError: If amount is not greater than 0.
        """
        pass

    @abstractmethod
    def withdraw(self, amount):
        """
        Withdraw a given amount into the account.

        Args:
            amount (float): Amount to withdraw, must be greater than 0.

        Raises:
            ValueError: If amount is not greater than 0 or no enough money on the account.
        """
        pass

