'''
3. Look at the following description of a problem domain:
The bank offers the following types of accounts to its customers: savings accounts,
checking accounts, and money market accounts. Customers are allowed to deposit money
into an account (thereby increasing its balance), withdraw money from an account (thereby
decreasing its balance), and earn interest on the account. Each account has an interest rate.
Assume that you are writing a program that will calculate the amount of interest earned for a
bank account.
Identify the potential classes in this problem domain.
Refine the list to include only the necessary class or classes for this problem.
Identify the responsibilities of the class or classes.


1) Identify the potential classes in this problem domain.
In my solution I declared two classes account "Type" and "Account"
    
2) Refine the list to include only the necessary class or classes for this problem.
It can be simplified by declaring static variables in the Account class instead of using enum

3) Identify the responsibilities of the class or classes.
Type class - An enumeration is a set of symbolic names (members) bound to unique, constant values. 
    Within an enumeration, the members can be compared by identity, and the enumeration itself can be iterated over.
Account class - Represents the available methods for manipulating a client's balance.

>> python hw3_exercise3.py

Acccount: Type.SAVINGS, Last Balance: $100,000
After interest: Acccount: Type.SAVINGS, Last Balance: $102,500.0
Acccount: Type.CHECKING, Last Balance: $550
Acccount: Type.MONEY_MARKET, Last Balance: $100,600
After interest: Acccount: Type.MONEY_MARKET, Last Balance: $108,145.0
'''
from enum import Enum

class Type(Enum):
    SAVINGS = 1
    CHECKING = 2
    MONEY_MARKET = 3

class Account:
    def __init__(self, account: Type, balance: float, interestRate = .5):
        self.__account = account
        self.__balance = balance
        self.__interest = interestRate
    
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def interest(self, timeYears):
        self.__balance += (self.__balance * timeYears * self.__interest) / 100
    

    def __str__(self):
       return "Acccount: {}, Last Balance: ${:,}".format(self.__account, self.__balance)

def main():
    account1 = Account(Type.SAVINGS, 100000)
    print(account1)
    account1.interest(5)
    print("After interest:", account1)

    account2 = Account(Type.CHECKING, 500)
    account2.deposit(100)
    account2.withdraw(50)
    print(account2)

    account3 = Account(Type.MONEY_MARKET, 100000, 1.5)
    account3.deposit(600)
    print(account3)
    account3.interest(5)
    print("After interest:", account3)

if __name__ == "__main__":
    main()