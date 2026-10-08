class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute
        
    def display_balance(self):
        print(f"Balance: {self.__balance}")

account = BankAccount(40000)

account.display_balance()