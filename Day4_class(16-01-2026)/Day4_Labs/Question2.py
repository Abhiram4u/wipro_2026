# Topics: Parameterized Methods, Constructors & Destructors
# Create a class BankAccount that:
# 1. Uses a parameterized constructor to initialize account_number and balance
class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance

        # 2. Implements methods deposit(amount) and withdraw(amount)
    def deposit(self,amount):
        self.balance += amount
        print("amount deposited successfully, current balance: ",self.balance)
    def withdraw(self,amount):
        # Handle invalid withdrawal using proper checks
        if self.balance >= amount:
            self.balance -= amount
            print("amount withdrawd successfully, current balance: ",self.balance)
        else:
            print("insufficient funds")

    # 3. Uses a destructor to display a message when the object is deleted
    def __del__(self):
        print("Account is deleted")


ac1 = BankAccount(1234,5000)
ac1.deposit(100)
ac1.withdraw(100)



