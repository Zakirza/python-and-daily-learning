#Access modifiers in python
#public, private, protected

from random import randint
class Bank:
    def __init__(self)->None:
        self.__account_number = randint(10000,99999)
        self.name=input("Enter your name: ")
        self.__balance=0

    def balance_display(self):      ##getter method to access private variable
        print("Your balance is: ",self.__balance)

    def setbalance(self,amount):   ##setter method to set the value of private variable
        self.__balance=amount

    def show_info(self):
        print("Account Number: ",self.__account_number)
        print("Name: ",self.name)
        print("Balance: ",self.__balance)

obj=Bank()
obj.show_info()
obj.__account_number=1
obj.__balance=1000 ##is not possible to change the value of private variable from outside the class
obj.show_info()
obj.setbalance(1000) ##setter method to set the value of private variable
obj.balance_display()
print(obj._Bank__balance) ##accessing private variable using name mangling


