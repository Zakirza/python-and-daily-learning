class Father:
    def __init__(self):
        self.father_name=input("Enter your father name: ")
        self._balance=int(input("Enter your balance: "))
        self.__phone_model=input("Enter your phone model: ")

    def __str__(self)->str:
        return f"Father: {self.father_name}, Balance: {self._balance}, Phone: {self.__phone_model}"

    def display(self):
        print("Father name: ",self.father_name)
        print("Balance: ",self._balance)
        print("Phone Model: ",self.__phone_model)


object=Father()
print(object)
