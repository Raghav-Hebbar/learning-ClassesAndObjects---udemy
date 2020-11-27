accountNo = input("Enter Account Number:")
customerName = input("Enter Customer Name:")
accountType = input("Enter Account Type:")
balance = float(input("Enter Balance :"))

def showAccount():
    print("Account # :{}\ncustomerName: {}\nacountType: {}\nbalance: {}".format(accountNo, customerName, 
    accountType,balance))

def withDraw(balance, amount):
    if accountType == "SAVINGS":
        newBalance = balance - amount
        if newBalance < 500:
            raise Exception("Insufficent Balance Cannot withdraw amount")
        else:
            balance = newBalance
            return balance
    elif accountType == "CURRENT":
        balance = balance - amount
        return balance  

showAccount()
amount = float(input("Enter the Amount to be withdrawn: "))
balance = withDraw(balance,amount)
print("after withdraw New balance:")
print("Balance :",balance)

# Traditional way of implimenting code 