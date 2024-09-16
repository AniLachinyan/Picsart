from abc import ABC,abstractmethod
from account import Account
class Account(ABC):
    def __init__(self,account_number:int, balance: float, account_type:str ):
        self.__account_number=account_number
        self.__balance=balance
        self.__account_type=account_type


    @abstractmethod
    def deposit(self,amount: float) -> None:
        pass

    @abstractmethod
    def withdraw(self,amount: float) ->None:
        pass
    
    @abstractmethod
    def transfer(self,destination: Account , amount: float) -> None:
        pass
    @abstractmethod
    def show_balance(self) -> None:
        pass

    @abstractmethod
    def get_account_type(self) -> str:
        pass     


    def getAccountNumber(self):
        return self.__account_number
    
    def setAccountNumber(self,account_number):
        if (type(account_number) is not int or account_number<0):
            print("Please enter a valid account number")
        self.__account_number=account_number    


    def getBalance(self):
        return self.__balance

    def setBalance(self,balance):
        if (balance<0 or not isinstance(balance,(int,float)) ):
            print("Please enter valid Account Balance")
        self.__balance=balance


    def getAccountType(self):
        return self.__account_type


    def setAccountNumber(self,account_type):
        if (type(account_type) is not str):
            print("Please enter valid Account Type")
        self.__account_type=account_type





class CheckingAccount(Account):
    def __init__(self, account_number: int, balance: float, account_type: str, overdraft_limit:float ):
        super().__init__(account_number, balance, account_type)
        self.__overdraft_limit=overdraft_limit

    def getOverdraftLimit(self):
        return self.__overdraft_limit
    
    def setOverdraftLimit(self,overdraft_limit):
        if (overdraft_limit > 0):
            self.__overdraft_limit=overdraft_limit
        else:
            print("Overdraft limit can't be negative")    

    def deposit(self, amount: float) -> None:
        self.__balance+=amount
        print(f"Deposited {amount}$. New balance is {self.__balance}$")

    def withdraw(self, amount: float) -> None:
        if (self.__balance - amount < -self.__overdraft_limit):
            print("Insuddicient funds, overdraft limit exceeded")
        else:
            self.__balances-=amount
            print(f"Withdrew {amount}$. New balnce is {self.__balance}$")    

    def transfer(self, destination: Account, amount: float) -> None:
            if (self.__balance - amount < -self.__overdraft_limit):
                print("Transfer failed: Insufficient funds,overdraft limit exceeded ")
            else:
                self.withdraw(amount)
                destination.deposit(amount)
                print(f"Transferred {amount}$ to {destination.__account_number} ")
                print(f"Your new balance is {self.__balance}$")

    def show_balance(self) -> None:
        print(f"Your account balance is {self.__balance}$")


    def get_account_type(self) -> str:
        return self.__account_type
    
class SavingsAccount(Account):
    def __init__(self, account_number: int, balance: float, account_type: str, interest_rate: float):
            super().__init__(account_number, balance, account_type)
            self.__interest_rate=interest_rate



    def deposit(self, amount: float) -> None:
        self.__balance+=amount
        print(f"Deposited {amount}$. New balance is {self.__balance}$")

    def withdraw(self, amount: float) -> None:
        if (self.getBalance < amount ):
            print("Insufficient funds, overdraft limit exceeded")
        else:
            self.setBalance(self.getBalance-amount)
            print(f"Withdrew {amount}$. New balnce is {self.__balance}$")    

    def transfer(self, destination: Account, amount: float) -> None:
            if (self.__balance < amount ):
                print("Transfer failed: Insufficient funds,overdraft limit exceeded ")
            else:
                self.withdraw(amount)
                destination.deposit(amount)
                print(f"Transferred {amount}$ to {destination.__account_number} ")
                print(f"Your new balance is {self.__balance}$")

    def show_balance(self) -> None:
        print(f"Your account balance is {self.__balance}$")


    def get_account_type(self) -> str:
        return self.__account_type
    

    def apply_interest(self) -> None:
        interest_amount = self.__balance * (self.__interest_rate / 100)
        self.__balance += interest_amount
        print(f"Applied interest: ${interest_amount}. New balance: ${self.__balance}.")

class JointAccount(Account):
    def __init__(self, account_number: int, balance: float, account_type: str, joint_owners: list):
        super().__init__(account_number, balance, account_type)
        self.__joint_owners=joint_owners


    def add_owner(self, customer_name: str) -> None:
        self.__joint_owners.append(customer_name)
        print(f"Added {customer_name} as a joint owner.")


    def deposit(self, amount: float) -> None:
        self.__balance+=amount
        print(f"Deposited {amount}$. New balance is {self.__balance}$")

    def withdraw(self, amount: float) -> None:
        if (self.__balance < amount ):
            print("Insuffcient funds, overdraft limit exceeded")
        else:
            self.__balances-=amount
            print(f"Withdrew {amount}$. New balnce is {self.__balance}$")    

    def transfer(self, destination: Account, amount: float) -> None:
            if (self.__balance < amount ):
                print("Transfer failed: Insufficient funds,overdraft limit exceeded ")
            else:
                self.withdraw(amount)
                destination.deposit(amount)
                print(f"Transferred {amount}$ to {destination.__account_number} ")
                print(f"Your new balance is {self.__balance}$")

    def show_balance(self) -> None:
        print(f"Your account balance is {self.__balance}$")


    def get_account_type(self) -> str:
        return self.__account_type




    



        




    

