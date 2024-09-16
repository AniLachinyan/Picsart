from account.account import Account
from transfer.transaction import Transaction



class Customer:
    def __init__(self, name : str, contact_info : str, accounts: list[Account]):
        self.__name=name
        self.__contact_info=contact_info
        self.__accounts=accounts
        self.__transactions=[]


    def getName(self):
        return self.__name

    def setName(self,name):
        if (isinstance(name,str)):
            self.__name=name
        else:
            print("Please enter valid name")


    def getContactInfo(self):
        return self.__contact_info

    def setContactInfo(self,contact_info):
        if (isinstance(contact_info,str)):
            self.__contact_info=contact_info
        else:
            print("Please enter valid info")


    def getAccounts(self):
        return self.__accounts

    def setAccounts(self,accounts):
        if (isinstance(accounts,list)):
            self.__accounts=accounts
        else:
            print("Please enter valid accounts")


    def add_account(self,account : Account)->None:
        self.__accounts.append(account)

    def view_accounts(self)->None:
        if not self.__accounts:
            print("No accounts found")
        else:    
            for account in self.__accounts:
                print(account)

    def add_transaction(self,transaction : Transaction)->:
        self.__transactions.append(transaction)        

    def get_transaction_history(self)->list:
        return self.__transactions

    def view_transaction_history(self)->None:
        for account in self.__accounts:
            transactions=account.get_transaction_history()
            if not transactions:
                print("No transaction found")
            else:
                for transaction in transactions:
                    print(f"From: {transaction.getFromAccount().getAccountNumber()}, To: {transaction.getToAccount().getAccountNumber()}, Amount: {transaction.getAmount()}, Type: {transaction.getTransactionType()}, Date: {transaction.getTimeStamp()}")    

