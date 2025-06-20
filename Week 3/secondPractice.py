# Practice
# Create Account class with 2 attribute - balance and account no.
# Create methods for credit, debite & printing the balance.
class Account:

    def __init__(self,account_no):
        self.account_no = account_no
        self.balance = 0

    def debite(self):
        print("*"*10,"\nDebite","\n"+"*"*10)
        amount = int(input("Enter the amount to debite on your account: "))

        self.balance += amount
        print("Successfully amount debited.")
    
    def credit(self):
        print("*"*10,"\nCredit","\n"+"*"*10)
        account = input("Enter the account no: ")
        amount = int(input("Enter the amount: "))

        if (self.balance - amount) > 0:
            self.balance -= amount
            print(f"{amount} credited on {account}. your avaibale balance {self.balance}")
        else:
            print("oops! sorry check your balance!!")

    def getBalance(self):
        print(f"{self.account_no} is available balance: {self.balance}")

    def getAccountNo(self):
        print(f"Your account no: {self.account_no}")

    @staticmethod
    def menu():
        print("="*15)
        print("ABC Bank")
        print("="*15)
        print("Press 1 for Debit")
        print("Press 2 for Credit")
        print("Press 3 for check balance")
        print("Press 4 for check account no")
        print("Press 5 for exit")

        return int(input("Enter your choice: "))

if __name__ == "__main__":
    account_no = input("Enter your account no: ")
    a1 = Account(account_no)
    
    while True:
        ch = Account.menu()

        if ch == 1:
            a1.debite()
        elif ch == 2:
            a1.credit()
        elif ch == 3:
            a1.getBalance()
        elif ch == 4:
            a1.getAccountNo()
        elif ch == 5:
            break
        else:
            print("Wrong choice!!")
            if input("Do you want to countinue to 'Y' either 'N': ") != 'Y':
                break