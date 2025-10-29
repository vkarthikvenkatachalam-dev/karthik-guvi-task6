class BankAccount:
    def __init__(self,Account_no,balance=0):
        self.Account_no = Account_no
        self.__balance= balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit ₹{amount}.new_balance:₹{self.__balance}")
        else:
            print("maintain positive balance")

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}.new_balance:₹{self.__balance}")
        else:
            print("maintain min balance")
    def get_balance(self):
        return self.__balance
    







