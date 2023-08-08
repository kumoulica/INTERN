class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin

class Transaction:
    def __init__(self, amount, transaction_type):
        self.amount = amount
        self.transaction_type = transaction_type

class ATM:
    def __init__(self):
        self.users = []  # List of User objects
        self.transactions = []  # List of Transaction objects
        self.current_user = None

    def add_user(self, user_id, pin):
        user = User(user_id, pin)
        self.users.append(user)

    def authenticate_user(self, user_id, pin):
        for user in self.users:
            if user.user_id == user_id and user.pin == pin:
                self.current_user = user
                return True
        return False

    def display_menu(self):
        print("ATM Menu:")
        print("1. Transactions History")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Quit")

    def process_choice(self, choice):
        if choice == 1:
            self.display_transactions_history()
        elif choice == 2:
            self.withdraw()
        elif choice == 3:
            self.deposit()
        elif choice == 4:
            self.transfer()
        elif choice == 5:
            self.quit()
        else:
            print("Invalid choice!")

    def display_transactions_history(self):
        print("Transactions History:")
        for transaction in self.transactions:
            print(f"Amount: {transaction.amount}, Type: {transaction.transaction_type}")

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        if amount > 0:
            self.transactions.append(Transaction(amount, "Withdraw"))
            print("Withdrawal successful!")
        else:
            print("Invalid amount!")

    def deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
            self.transactions.append(Transaction(amount, "Deposit"))
            print("Deposit successful!")
        else:
            print("Invalid amount!")

    def transfer(self):
        amount = float(input("Enter the amount to transfer: "))
        if amount > 0:
            self.transactions.append(Transaction(amount, "Transfer"))
            print("Transfer successful!")
        else:
            print("Invalid amount!")

    def quit(self):
        print("Quitting...")
        exit()


# Usage example
atm = ATM()
atm.add_user("1234", "5678")  # Add a user with user id "1234" and pin "5678"

user_id = input("Enter your user id: ")
pin = input("Enter your pin: ")

if atm.authenticate_user(user_id, pin):
    while True:
        atm.display_menu()
        choice = int(input("Enter your choice: "))
        atm.process_choice(choice)
else:
    print("Authentication failed!")
