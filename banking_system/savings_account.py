from banking_system.BankAccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self,Account_no,Initial_balance=0,Interest_rate=0.05):
        super().__init__(Account_no,Initial_balance)
        self.interest_rate=Interest_rate


    def calculate_interest(self):
        interest = self.get_balance()*self.interest_rate
        print(f"Interest_amount ₹{interest}")
        return interest








