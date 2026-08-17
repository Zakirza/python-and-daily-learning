class Father:
    def __init__(self):
        self.father_name=input("Enter your father name: ")
        self._balance=int(input("Enter your balance: "))
        self.__phone_model=input("Enter your phone model: ")

    def display(self):
        print("Father name: ",self.father_name)
        print("Balance: ",self._balance)
        print("Phone Model: ",self.__phone_model)

class Son(Father):
    def __init__(self):
        super().__init__()
        self.son_name=input("Enter your son name: ")

    def display(self):
        print("Son name: ",self.son_name)
        print("Father name: ",self.father_name)
        print("Balance: ",self._balance)

child=Son()
child.display()