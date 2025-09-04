from datetime import datetime

from .abstract_bank_account import AbstractBankAccount
from .mixins import AccountInfoMixin


class BaseBankAccount(AbstractBankAccount, AccountInfoMixin):

    accounts = 0   # static attribute

    def __init__(self, name, email, balance):
        self.name = name
        self._email = email
        self._balance = self._validate_balance(balance)
        self.creation_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        type(self).accounts += 1

    
    @property                           # getter for protected attribute email
    def email(self):
        return self._email
    
    @email.setter                        # setter for protected attribute email
    def email(self, new_email):
        if '@' in new_email:
            print(f"Email changed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            self._email = new_email

    @property                           # getter for protected attribute email
    def balance(self):
        return self._balance
    

    def creation_message(self) -> str:
        message = f"{self.account_type.capitalize()} account for {self.name} has been created."
        if self.TRANSACTION_FEES:
            message += " Notice that"
            for trans_type, trans_fee in self.TRANSACTION_FEES.items():
                message += f" for each {trans_type.upper()} there's a fee of {trans_fee}$"
        return message


    def deposit(self, amount):        
        if self._validate_amount("deposit", amount):
            self._balance += amount
            print(type(self).log_transaction("deposit", amount))
        else:
            raise ValueError("Amount must be greater than 0")
        
    def withdraw(self, amount):
        if self._validate_amount("withdraw", amount):
            self._balance -= amount
            print(type(self).log_transaction("withdraw", amount))
        else:
            raise ValueError(
                f"Invalid withdrawal: amount must be greater than 0, "
                f"and your balance must be at least {amount + type(self).MIN_BALANCE}$ "
                f"to keep the minimum balance of {type(self).MIN_BALANCE}$."
            )

    def _validate_balance(self, balance):
        if balance >= type(self).MIN_BALANCE:
            return balance
        raise ValueError(f"Minimum balance allowed for creating account is {type(self).MIN_BALANCE}$")
    
    def _validate_amount(self, transaction_type, amount):
        if transaction_type == "deposit":
            return amount > 0

        if transaction_type == "withdraw":
            return amount > 0 and self._balance >= amount + type(self).MIN_BALANCE
        
        raise ValueError("Invalid transaction type")
        

    @classmethod
    def log_transaction(cls, transaction_type, transaction_amount):
        transaction_msg = f"[{cls.__name__}]: New transaction of type {transaction_type.upper()} with amount {transaction_amount}$"
        if hasattr(cls, "TRANSACTION_FEES") and transaction_type in cls.TRANSACTION_FEES:
            transaction_msg += f" plus {cls.TRANSACTION_FEES[transaction_type]}$ fees."

        return transaction_msg