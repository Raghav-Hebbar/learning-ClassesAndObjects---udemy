from abc import ABC, abstractmethod

class Account():
    def __init__(self, accountNo, customerName, accountType, balance):
        self.AccountNo = accountNo
        self.CustomerName = customerName
        self.AccountType = accountType
        self.Balance = balance

    def __str__(self):
        return "Account # :{}\ncustomerName: {}\nacountType: {}\nbalance: {}".format(self.AccountNo,
        self.CustomerName, self.AccountType, self.Balance)

    def Deposit(self, amount):
        self.Balance += amount

    @abstractmethod
    def withDraw(self, amount): pass

class SavingsAccount(Account):
    def withDraw(self, amount):
        if(self.Balance - amount) < 500:
            raise Exception("Insufficent Balance Cannot withdraw amount")
        else:   
            self.Balance -= amount

class CurrentAccount(Account):
    def withDraw(self, amount):
        self.Balance -= amount


sa = SavingsAccount(101, "shaker","SAVINGS" ,15000)
print(sa)
amount = float(input(" Enter amount to be withdrawn :"))
sa.withDraw(amount)
print("current balance: ",sa.Balance)

ca = CurrentAccount(101, "shaker","CURRENT", 15000)
print(ca)
amount = float(input(" Enter amount to be withdrawn :"))
ca.withDraw(amount)
print("current balance: ",ca.Balance)

da = Account(101, "shaker","SAVINGS" ,15000)
print(da)
da.Deposit(5000)
print("Available Balance :",da.Balance)
