from random import randint


class Bank:
    def __init__(self)->None:
        self.fullname = input("Enter name = ")
        self.account_no=randint(100000, 999999)
        self.balance=0
        self.phone_no=int(input("Enter phone number = ")) 


    def show_bal(self)->None:
        print(f"Account holder: {self.fullname}, Account number: {self.account_no}, Balance: {self.balance}, Phone number: {self.phone_no}" )  

    def check_balance(self)->None:
        print(f"Your balance is {self.balance}")

    def withdraw(self)->None:
        amount=int(input("Enter amount to withdraw = "))
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
            print(f"Withdrawn {amount}. New balance is {self.balance}")

    def deposit(self)->None:
        amount=int(input("Enter amount to deposit = "))
        self.balance+=amount
        print(f"Deposited {amount}. New balance is {self.balance}") 

"""b1=Bank()
b1.show_bal()
b1.deposit()
b1.show_bal()
b1.withdraw()
b1.show_bal()"""


banks = []


def find_account(account_no: int):
    for acc in banks:
        if acc.account_no == account_no:
            return acc
    return None


while True:
    print("\n1. Create account")
    print("2. Show all bank details")
    print("3. Check balance")
    print("4. Withdraw")
    print("5. Deposit")
    print("6. Transfer")
    print("7. Exit")
    try:
        choice = int(input("Enter your choice = "))
    except ValueError:
        print("Please enter a valid number for choice")
        continue

    if choice == 1:
        account = Bank()
        banks.append(account)
        print(f"Account created with number: {account.account_no}")

    elif choice == 2:
        if not banks:
            print("No accounts found")
        else:
            for account in banks:
                account.show_bal()

    elif choice == 3:
        if not banks:
            print("No accounts found")
            continue
        try:
            account_no = int(input("Enter account number = "))
        except ValueError:
            print("Invalid account number")
            continue
        account = find_account(account_no)
        if account:
            account.check_balance()
        else:
            print("Account not found")

    elif choice == 4:
        if not banks:
            print("No accounts found")
            continue
        try:
            account_no = int(input("Enter account number = "))
        except ValueError:
            print("Invalid account number")
            continue
        account = find_account(account_no)
        if account:
            account.withdraw()
        else:
            print("Account not found")

    elif choice == 5:
        if not banks:
            print("No accounts found")
            continue
        try:
            account_no = int(input("Enter account number = "))
        except ValueError:
            print("Invalid account number")
            continue
        account = find_account(account_no)
        if account:
            account.deposit()
        else:
            print("Account not found")

    elif choice == 6:
        if not banks:
            print("No accounts found")
            continue
        try:
            from_account_no = int(input("Enter your account number = "))
            to_account_no = int(input("Enter account number to transfer = "))
        except ValueError:
            print("Invalid account number")
            continue
        from_account = find_account(from_account_no)
        to_account = find_account(to_account_no)
        if not from_account:
            print(f"From account {from_account_no} not found")
            continue
        if not to_account:
            print(f"To account {to_account_no} not found")
            continue
        try:
            amount = int(input("Enter amount to transfer = "))
        except ValueError:
            print("Invalid amount")
            continue
        if amount > from_account.balance:
            print("Insufficient balance")
        else:
            from_account.balance -= amount
            to_account.balance += amount
            print(f"Transferred {amount} from account {from_account_no} to account {to_account_no}")

    elif choice == 7:
        print("Goodbye")
        break

    else:
        print("Invalid choice, please try again")

