from .base_bank_account import BaseBankAccount

class BusinessAccount(BaseBankAccount):

    MIN_BALANCE = 5000
    TRANSACTION_FEES = {'withdraw': 10}   # static attribute, capital letters is a convention for constant
    MONTHLY_FEES = 1
    INTEREST_PERCENTAGE = 1


    def __init__(self, name, email, balance):
        super().__init__(name, email, balance)
        self.account_type = 'business'
        
        print(self.creation_message())


        
    def add_interest(self):
        interest_value = self._balance * (self.INTEREST_PERCENTAGE / 100)
        self._balance += interest_value
        print(f"Current balance after adding interests is {self._balance}")
    
    def cut_monthly_fees(self):
        self._balance -= self.MONTHLY_FEES
        print(f"Current balance after cutting monthly fees is {self._balance}")
    
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
        