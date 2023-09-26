from validation import *
class BankAccount:
    def __init__(self, bank_name, ifsc_code, account_number, account_holder_name, age, gender, dob, address, city, account_type, balance, pan_card_number, aadhar_number):
        self.bank_name = bank_name
        self.ifsc_code = ifsc_code
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.age = age
        self.gender = gender
        self.dob = dob
        self.address = address
        self.city = city
        self.account_type = account_type
        self.balance = balance
        self.pan_card_number = pan_card_number
        self.aadhar_number = aadhar_number
    def update_name(self, new_name):
        self.account_holder_name = new_name
    def update_address(self, new_address):
        self.address = new_address
    def update_dob(self, new_dob):
        self.dob = new_dob
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        return False
    def transfer_funds(self, recipient, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            return True
        return False
    def balance_enquiry(self):
        return self.balance
    def __str__(self):
        return f"Account Holder: {self.account_holder_name}\nAccount Number: {self.account_number}\nBalance: {self.balance}"


def create_account():
    bank_name = input("Enter Bank Name: ")
    ifsc_code = input("Enter IFSC code: ")
    ifsc_code=validate_ifsc_code(ifsc_code)
    while ifsc_code is False:
        print("Invalid IFSC code. Please enter a valid IFSC code. eg(AXIS0000123)")
        ifsc_code = input("Enter IFSC code: ")
        ifsc_code=validate_ifsc_code(ifsc_code)

    account_number = input("Enter Account Number: ")
    account_holder_name = input("Enter Account Holder Name: ")
    age = input("Enter Age: ")
    age = validate_age(age)
    while age is None:
        print("Invalid age. Age must be 18 or older.")
        age = input("Enter Age: ")
        age = validate_age(age)
    
    gender = input("Enter Gender: ")
    gender = validate_gender(gender)
    while gender is None:
        print("Invalid gender. Please enter 'Male', 'Female', or 'Other'.")
        gender = input("Enter Gender: ")
        gender = validate_gender(gender)
    address = input("Enter Address: ")
    city = input("Enter City: ")
    account_type = input("Enter Type of Account: ")
    balance = float(input("Enter Initial Balance: "))
    dob = input("Enter Date of Birth (DD-MM-YYYY): ")
    dob = validate_dob(dob)
    while dob is False:
        print("Invalid date of birth format. Please use DD-MM-YYYY format.")
        dob = input("Enter Date of Birth (DD-MM-YYYY): ")
        dob = validate_dob(dob)
    pan_card_number = input("Enter PAN Card Number: ")
    pan_card_number = validate_pan_card(pan_card_number)
    while pan_card_number is False:
        print("Invalid PAN card number format. Please use a valid format (e.g., ABCDE1234F).")
        pan_card_number = input("Enter PAN Card Number: ")
        pan_card_number =validate_pan_card(pan_card_number)
    aadhar_number = input("Enter Aadhar Number: ")
    aadhar_number = validate_aadhar_number(aadhar_number)
    while aadhar_number is False:
        print("Invalid Aadhar number format. Please use a 12-digit number.")
        aadhar_number = input("Enter Aadhar Number: ")
        aadhar_number = validate_aadhar_number(aadhar_number)
    account = BankAccount(bank_name, ifsc_code, account_number, account_holder_name, age, gender, dob,address, city, account_type, balance, pan_card_number, aadhar_number)
    accounts.append(account)
    print("Account created successfully.")



# Function to delete an account
def delete_account(account_number):
    for account in accounts:
        if account.account_number == account_number:
            accounts.remove(account)
            print(f"Account {account_number} has been deleted.")
            return
    print(f"Account {account_number} not found.")

# Function to search for an account by account number
def search_by_account_number(account_number):
    for account in accounts:
        if account.account_number == account_number:
            print(account)
            return
    print(f"Account {account_number} not found.")

# Function to update account details (choice 3)
def update_account_details():
    account_number = input("Enter Account Number to update: ")
    for account in accounts:
        if account.account_number == account_number:
            print("Select an option to update:")
            print("1. Update name of account holder")
            print("2. Update address of account holder")
            print("3. Update DOB of account holder")
            update_option = input("Enter your choice: ")
            if update_option == "1":
                new_name = input("Enter the new name: ")
                account.update_name(new_name)
                print("Name updated successfully.")

            elif update_option == "2":
                new_address = input("Enter the new address: ")
                account.update_address(new_address)
                print("Address updated successfully.")
            elif update_option == "3":
                new_dob = input("Enter the new Date of Birth (DD-MM-YYYY): ")
                account.update_dob(new_dob)
                print("Date of Birth updated successfully.")
            else:
                print("Invalid update option.")
            return
    print(f"Account {account_number} not found.")

# Function to deposit funds (choice 4)
def deposit_funds():
    account_number = input("Enter Account Number to deposit funds: ")
    for account in accounts:
        if account.account_number == account_number:
            amount = float(input("Enter the amount to deposit: "))
            if account.deposit(amount):
                print(f"Amount {amount} deposited successfully.")
            else:
                print("Invalid amount. Please enter a positive amount.")
            return
    print(f"Account {account_number} not found.")

# Function to withdraw funds (choice 5)
def withdraw_funds():
    account_number = input("Enter Account Number to withdraw funds: ")
    for account in accounts:
        if account.account_number == account_number:
            amount = float(input("Enter the amount to withdraw: "))
            if account.withdraw(amount):
                print(f"Amount {amount} withdrawn successfully.")
            else:
                print("Invalid amount or insufficient balance.")
            return
    print(f"Account {account_number} not found.")

def transfer_funds():
    sender_account_number = input("Enter your Account Number (Sender): ")
    recipient_account_number = input("Enter recipient's Account Number: ")
    for sender in accounts:
        if sender.account_number == sender_account_number:
            for recipient in accounts:
                if recipient.account_number == recipient_account_number:
                    amount = float(input("Enter the amount to transfer: "))
                    if sender.transfer_funds(recipient, amount):
                        print(f"Amount {amount} transferred successfully to Account {recipient_account_number}.")
                    else:
                        print("Invalid amount or insufficient balance.")
                    return
            print(f"Recipient account {recipient_account_number} not found.")
            return
    print(f"Sender account {sender_account_number} not found.")

# Function to search for an account by account holder name
def search_by_name(account_holder_name):
    found_accounts = []
    for account in accounts:
        if account.account_holder_name.lower() == account_holder_name.lower():
            found_accounts.append(account)
    
    if found_accounts:
        for account in found_accounts:
            print(account)
    else:
        print(f"No accounts found for account holder name: {account_holder_name}")

def search_by_account_type(account_type):
    found_accounts = []
    for account in accounts:
        if account.account_type.lower() == account_type.lower():
            found_accounts.append(account)
    
    if found_accounts:
        for account in found_accounts:
            print(account)
    else:
        print(f"No accounts found for account type: {account_type}")

# Function to perform a balance enquiry
def balance_enquiry(account_number):
    for account in accounts:
        if account.account_number == account_number:
            print(f"Balance for account {account_number}: {account.balance}")
            return
    print(f"Account {account_number} not found.")



accounts = []

while True:
    print("\nBank Account Management System")
    print("1. Create Account")
    print("2. Delete Account")
    print("3. Update Account Details")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Funds Transfer")
    print("7. Search details of account holder")
    print("8. Balance Enquiry")
    print("9. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        create_account()
    elif choice == "2":
        account_number = input("Enter Account Number to delete: ")
        delete_account(account_number)
    elif choice == "3":
        update_account_details()
    elif choice == "4":
        deposit_funds()
    elif choice == "5":
        withdraw_funds()
    elif choice == "6":
        transfer_funds()
    elif choice == "7":
        search_option = input("Select search criteria:\n1. Search by account number\n2. Search by name\n3. Search by Type of Account\nEnter Your Choice = ")
        if search_option == "1":
            account_number = input("Enter Account Number to search: ")
            search_by_account_number(account_number)
        elif search_option == "2":
            account_holder_name = input("Enter Account Holder Name to search: ")
            search_by_name(account_holder_name)
        elif search_option == "3":
            account_type = input("Enter Type of Account to search: ")
            search_by_account_type(account_type)
        else:
            print("Invalid search option.")
    elif choice == "8":
        account_number = input("Enter Account Number for balance enquiry: ")
        balance_enquiry(account_number)
    elif choice == "9":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")






