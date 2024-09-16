
from account.account import Account
from datetime import datetime


class Transaction:
    def __init__(self, from_account : Account , to_account : Account, amount : float, transaction_type : str, timestamp : datetime):
        self.__from_account=from_account
        self.__to_account=to_account
        self.__amount=amount
        self.__transaction_type=transaction_type
        self.__timestamp=timestamp



    def getFromAccount(self):
        return self.__from_account

    def setFromAccount(self,from_account):
        if (isinstance(from_account,Account)):
            self.__from_account=from_account
        else:
            print("Account is not valid")



    def getToAccount(self):
        return self.__to_account

    def setToAccount(self,to_account):
        if (isinstance(to_account,Account)):
            self.__to_account=to_account
        else:
            print("Account is not valid")          



    def getAmount(self):
        return self.__amount

    def setAmount(self,amount):
        if (isinstance(amount,float) and amount>0):
            self.__amount=amount
        else:
            print("Please enter valid amount") 


    def getTransactionType(self):
        return self.__transaction_type

    def setTransactionType(self,transaction_type):
        if (isinstance(transaction_type,str)):
            self.__transaction_type=transaction_type
        else:
            print("Invalid type")


    def getTimeStamp(self):
        return self.__timestamp

    def setTimeStamp(self,timestamp):
        if (isinstance(timestamp,datetime)):
            self.__timestamp=timestamp      
        else:
            print("Time is not valid")      



    def log(self)->None:
        print(f"Transaction is done by {self.__from_account} account")
        print(f"Transaction is done to {self.__to_account} account")
        print(f"Transaction amount is {self.__amount}$")
        print(f"Transaction type is {self.__transaction_type}")
        print(f"Transaction is done at {self.__timestamp} account")




