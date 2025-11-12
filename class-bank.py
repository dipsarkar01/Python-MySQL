class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def show_balance(self):
        print(f"Account Holder: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.balance}")

# Taking user input
name = input("Enter Customer Name: ")
account_number = input("Enter Account Number: ")

# Creating an account instance
account = BankAccount(name, account_number)

while True:
    print("\nOptions:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)
    elif choice == "3":
        account.show_balance()
    elif choice == "4":
        print("Exiting... Have a great day!")
        break
    else:
        print("Invalid option. Please try again.")