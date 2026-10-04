class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Enter a valid amount.")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid amount.")
        
        elif amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient Balance.")
    
    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")


account1 = BankAccount("Yash", 50000)

account1.deposit(25000)
account1.withdraw(20000)

account1.display_balance()
    
    
                  

    