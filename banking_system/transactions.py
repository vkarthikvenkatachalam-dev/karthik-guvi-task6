from banking_system.current_account import CurrentAccount
from banking_system.savings_account import SavingsAccount


class Transaction:
    def __init__(self):
        self.savings = SavingsAccount("SBVT123",7000,0.05)
        self.current = CurrentAccount("CVTV124",10000,2000)
    def perform_transactions(self):
        print("\n--- Savings Account Transactions ---")
        self.savings.deposit(5000)
        self.savings.calculate_interest()
        self.savings.withdraw(2000)

        print("\n--- Current Account Transactions ---")
        self.current.withdraw(2000)
        self.current.withdraw(3000)


txn = Transaction()
txn.perform_transactions()


