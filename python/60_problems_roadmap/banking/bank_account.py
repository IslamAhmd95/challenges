from .base_bank_account import BaseBankAccount


class BankAccount(BaseBankAccount):

    MIN_BALANCE = 20   # static attribute, capital letters is a convention for constant
    TRANSACTION_FEES = dict()   # static attribute, capital letters is a convention for constant

    def __init__(self, name, email, balance):
        super().__init__(name, email, balance)
        self.account_type = "regular"
        
        print(self.creation_message())


    
