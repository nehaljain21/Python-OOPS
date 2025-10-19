class BankAccount:
    total_balance = 0

    def __init__(self, owner_name, balance=0):
        self.owner_name = owner_name
        self.__balance = balance
        BankAccount.total_balance += balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            BankAccount.total_balance += amount
            print(f"{amount} deposited. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            BankAccount.total_balance -= amount
            print(f"{amount} withdrawn. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")
    
    @property
    def get_balance(self):
        return self.__balance
    
    @classmethod
    def get_total_balance(cls):
        return cls.total_balance
    
    @staticmethod
    def account_exists(account_number):
        existing_account_numbers = ['12345', '67890', '54321']
        if account_number in existing_account_numbers:
            return True
        return False
    

acc1=BankAccount("Alice", 1000)
acc2=BankAccount("Bob", 500)
print(f"Alice's balance: {acc1.get_balance}")
print(f"Bob's balance: {acc2.get_balance}")