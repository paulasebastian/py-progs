class BankAccount:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"\nSuccessfully deposited: Rs. {amount}")
        print(f"Updated Balance: Rs. {self.balance}\n")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"\nSuccessfully withdrew: Rs. {amount}")
            print(f"Updated Balance: Rs. {self.balance}\n")
        else:
            print(f"\nFailed to withdraw Rs. {amount}: Insufficient Balance!\n")

    def display_details(self):
        print("\n--- Account Details ---")
        print(f"Account Number : {self.acc_no}")
        print(f"Account Holder : {self.name}")
        print(f"Account Type   : {self.acc_type}")
        print(f"Current Balance: Rs. {self.balance}")
        print("-----------------------\n")

print("=== Create a New Bank Account ===")
user_acc_no = input("Enter Account Number: ")
user_name = input("Enter Account Holder Name: ")
user_type = input("Enter Account Type (e.g., Savings/Current): ")
user_balance = float(input("Enter Initial Balance: Rs. "))

my_account = BankAccount(user_acc_no, user_name, user_type, user_balance)

my_account.display_details()

dep_amt = float(input("Enter amount to deposit: Rs. "))
my_account.deposit(dep_amt)

with_amt = float(input("Enter amount to withdraw: Rs. "))
my_account.withdraw(with_amt)

my_account.display_details()