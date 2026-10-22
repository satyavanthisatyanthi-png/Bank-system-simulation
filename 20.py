class Account:
    def __init__(self, id, holder_name):
        self.id = id
        self.holder_name = holder_name
        self.balance = 100000 # initial

    def check_balance(self):
        print(f"Balance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} Deposited Successfully. Updated Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} Withdrawal Successful. New Balance: {self.balance}")
        else:
            print("Insufficient balance - less than in your account")

class SavingAccount(Account):
    INTEREST_RATE = 0.04  # 4%

    def calculate_interest(self):
        interest = self.balance * self.INTEREST_RATE
        print(f"Interest Calculated: {interest}")
        return interest

class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 5000

    def withdraw(self, amount):
        if self.balance + self.OVERDRAFT_LIMIT >= amount:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: {self.balance}")
        else:
            print("Still over overdraft limit")

class Bank:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.accounts = {}

    def create_account(self, id, holder_name, acc_type):
        if acc_type == "saving":
            new_account = SavingAccount(id, holder_name)
        elif acc_type == "current":
            new_account = CurrentAccount(id, holder_name)
        else:
            print("Invalid account type")
            return None
        
        self.accounts[id] = new_account
        print(f"Account creation successful - {id}")
        return new_account

    def get_account(self, id):
        if id not in self.accounts:
            print(f"Account {id} not found!")
            return None
        else:
            return self.accounts[id]

# --- Testing ---
SBI = Bank("State Bank of Karnataka", "Yelahanka")

S1 = SBI.create_account("1", "Aakash", "saving")
C1 = SBI.create_account("2", "Avinash", "current")

S1.deposit(1000)
C1.deposit(100)

S1.withdraw(2000)  # will show insufficient
C1.withdraw(20)

S1.calculate_interest()