from banking_system.BankAccount import BankAccount


class CurrentAccount(BankAccount):
    def __init__(self,Account_no,Initial_balance=0,min_balance=2000):
        super().__init__(Account_no,Initial_balance)
        self.min_balance = min_balance

    def withdraw(self,amount):
        if self.get_balance()-amount >= self.min_balance:
            super().withdraw(amount)
        else:
            print(f"Cannot withdraw ₹{amount}.Minimum_balance is {self.min_balance}")










