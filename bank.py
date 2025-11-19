class Bank:
    def __init__(self, acc_no, acc_name, acc_type, acc_bal):
        self.acc_no = acc_no
        self.name = acc_name
        self.acc_type = acc_type
        self.bal = acc_bal

    def deposit(self, amount):
        if amount <= 0:
            print("It should be a positive number")
        else:
            self.bal += amount
            print("Your current balance is:", self.bal)

    def withdraw(self, amount):
        if amount <= 0:
            print("It should be a positive number")
        elif amount > self.bal:
            print("Insufficient balance")
        else:
            self.bal -= amount
            print("Your current balance is:", self.bal)

    def display(self):
        print(f"Account number: {self.acc_no}")
        print(f"Account holder: {self.name}")
        print(f"Account type: {self.acc_type}")
        print(f"Current balance: {self.bal}")


no = int(input("Enter the account number: "))
name = input("Enter your name: ")
account_type_input = input("Enter your account type: ")
bal = int(input("Enter your balance: "))

user1 = Bank(no, name, account_type_input, bal)

while True:
    print("\n1) DEPOSIT\n2) WITHDRAW\n3) ACCOUNT INFORMATION\n4) EXIT\n")
    opt = int(input("Enter the option: "))

    if opt == 1:
        deposit_amt = int(input("Enter the amount to deposit: "))
        user1.deposit(deposit_amt)
    elif opt == 2:
        withdraw_amt = int(input("Enter the amount to withdraw: "))
        user1.withdraw(withdraw_amt)
    elif opt == 3:
        user1.display()
    elif opt == 4:
        print("Exiting...")
        break
    else:
        print("Invalid option")
