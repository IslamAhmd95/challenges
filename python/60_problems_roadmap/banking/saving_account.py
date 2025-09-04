from .base_bank_account import BaseBankAccount


class SavingAccount(BaseBankAccount):

    MIN_BALANCE = 40   # static attribute, capital letters is a convention for constant
    TRANSACTION_FEES = {'withdraw': 1}   # static attribute, capital letters is a convention for constant

    def __init__(self, name, email, balance):
        super().__init__(name, email, balance)
        self.account_type = "saving"
        
        print(self.creation_message())

        
        

    def withdraw(self, amount):
        if self._validate_amount("withdraw", amount + self.TRANSACTION_FEES['withdraw']):
            self._balance -= amount + self.TRANSACTION_FEES['withdraw']
            print(super().log_transaction("withdraw", amount))
        else:
            raise ValueError(
                f"Invalid withdrawal: amount must be greater than 0, "
                f"and your balance must be at least {amount + self.MIN_BALANCE + self.TRANSACTION_FEES['withdraw']}$ "
                f"to keep the minimum balance of {self.MIN_BALANCE}$."
            )
        
        
        

