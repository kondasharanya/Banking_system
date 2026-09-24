import random
from datetime import datetime
accounts = {}
def create_account():
    print("\n CREATE ACCOUNT ")
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    pin = input("Create a 4-digit PIN: ")
    if len(pin) != 4 or not pin.isdigit():
        print("PIN must contain exactly 4 digits.")
        return
    account_number = str(random.randint(100000, 999999))
    while account_number in accounts:
        account_number = str(random.randint(100000, 999999))
    accounts[account_number] = {
        "name": name,
        "phone": phone,
        "pin": pin,
        "balance": 0.0,
        "transactions": []
    }

    print("\nAccount created successfully!")
    print("Your Account Number:", account_number)
    print("Please remember your account number and PIN.")
def login():
    print("\n LOGIN ")
    account_number = input("Enter Account Number: ")
    pin = input("Enter PIN: ")
    if account_number in accounts:
        if accounts[account_number]["pin"] == pin:
            print("\nLogin successful!")
            print("Welcome,", accounts[account_number]["name"])
            account_menu(account_number)
        else:
            print("Incorrect PIN.")
    else:
        print("Account not found.")
def account_menu(account_number):
    while True:
        print("\n ACCOUNT MENU ")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Change PIN")
        print("7. Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            check_balance(account_number)
        elif choice == "2":
            deposit(account_number)
        elif choice == "3":
            withdraw(account_number)
        elif choice == "4":
            transfer(account_number)
        elif choice == "5":
            transaction_history(account_number)
        elif choice == "6":
            change_pin(account_number)
        elif choice == "7":
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice. Please try again.")
def check_balance(account_number):
    balance = accounts[account_number]["balance"]
    print("\n BALANCE ")
    print("Current Balance: ₹", balance)
def deposit(account_number):
    print("\n DEPOSIT ")
    amount = input("Enter amount to deposit: ")
    if not amount.replace(".", "", 1).isdigit():
        print("Please enter a valid amount.")
        return
    amount = float(amount)
    if amount <= 0:
        print("Amount must be greater than zero.")
        return
    accounts[account_number]["balance"] += amount
    transaction = (
        f"Deposit: ₹{amount} | "
        f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
    )
    accounts[account_number]["transactions"].append(transaction)
    print("₹", amount, "deposited successfully.")
    print("New Balance: ₹", accounts[account_number]["balance"])
def withdraw(account_number):
    print("\n WITHDRAW ")
    amount = input("Enter amount to withdraw: ")
    if not amount.replace(".", "", 1).isdigit():
        print("Please enter a valid amount.")
        return
    amount = float(amount)
    if amount <= 0:
        print("Amount must be greater than zero.")
        return
    current_balance = accounts[account_number]["balance"]
    if amount > current_balance:
        print("Insufficient balance.")
        return
    accounts[account_number]["balance"] -= amount
    transaction = (
        f"Withdrawal: ₹{amount} | "
        f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
    )
    accounts[account_number]["transactions"].append(transaction)
    print("₹", amount, "withdrawn successfully.")
    print("Remaining Balance: ₹", accounts[account_number]["balance"])
def transfer(account_number):
    print("\n TRANSFER MONEY ")
    receiver = input("Enter receiver Account Number: ")
    if receiver not in accounts:
        print("Receiver account not found.")
        return
    if receiver == account_number:
        print("You cannot transfer money to your own account.")
        return
    amount = input("Enter amount to transfer: ")
    if not amount.replace(".", "", 1).isdigit():
        print("Please enter a valid amount.")
        return
    amount = float(amount)
    if amount <= 0:
        print("Amount must be greater than zero.")
        return
    if amount > accounts[account_number]["balance"]:
        print("Insufficient balance.")
        return
    accounts[account_number]["balance"] -= amount
    accounts[receiver]["balance"] += amount
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    sender_transaction = (
        f"Transfer to Account {receiver}: ₹{amount} | {current_time}"
    )
    receiver_transaction = (
        f"Received from Account {account_number}: ₹{amount} | {current_time}"
    )
    accounts[account_number]["transactions"].append(
        sender_transaction
    )
    accounts[receiver]["transactions"].append(
        receiver_transaction
    )
    print("Transfer successful!")
    print("₹", amount, "transferred successfully.")
def transaction_history(account_number):
    print("\n TRANSACTION HISTORY ")
    transactions = accounts[account_number]["transactions"]
    if len(transactions) == 0:
        print("No transactions available.")
        return
    for number, transaction in enumerate(transactions, start=1):
        print(number, ".", transaction)
def change_pin(account_number):
    print("\n CHANGE PIN ")
    old_pin = input("Enter old PIN: ")
    if old_pin != accounts[account_number]["pin"]:
        print("Incorrect old PIN.")
        return
    new_pin = input("Enter new 4-digit PIN: ")
    if len(new_pin) != 4 or not new_pin.isdigit():
        print("PIN must contain exactly 4 digits.")
        return
    confirm_pin = input("Confirm new PIN: ")
    if new_pin != confirm_pin:
        print("PINs do not match.")
        return
    accounts[account_number]["pin"] = new_pin
    print("PIN changed successfully.")
def main():
    while True:
        print("\n")
        print("BANKING SYSTEM")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print("\nThank you for using Banking System!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")
main()