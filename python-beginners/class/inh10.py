class Account:
    def __init__(self):
        print("Account created")
class SavingsAccount(Account):
    def __init__(self):
        super().__init__()
        print("Savings Account created")
c=SavingsAccount()
