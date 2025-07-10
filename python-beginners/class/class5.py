class BankAccount:
    def __init__(self, account_holder):
        self.account_holder=account_holder
        self.balance=0
    def deposit(self):
        amount=int(input("enter "))
        self.balance+=amount
        print(self.balance)
    def withdraw(self):
        amount=int(input("enter "))
        self.balance-=amount
        print(self.balance)
    def display(self):
        print(self.balance)
b1=BankAccount("abc")
inp=int(input("1 for display, 2 for deposit, 3 for withdraw "))
if inp==1:
    b1.display()
elif inp==2:
    b1.deposit()
elif inp==3:
    b1.withdraw()