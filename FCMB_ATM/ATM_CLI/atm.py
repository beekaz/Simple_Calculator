from account import Account
import random
import json

account_list =[]
def user_info():
    first_name= input("Enter your first name: ")
    last_name= input("Enter your last name: ")
    date_of_birth= input("Enter date of birth: ")
    age= input("How old are you: ")
    email=input("Enter email address: ")
    
    return first_name, last_name, date_of_birth, age, email

def account_details():
    first_name, last_name, date_of_birth, age, email = user_info()
    account_number = generate_account_number()
    print("\nCongratulation you've created an account with Us\nYou've being automatically credited 1000")
    print(f"Name: {first_name} {last_name}\nEmail: {email}")
    print(f"Account Number: {account_number}")
    
def account_storage():
    new_account= account_details()
    account_list.append(new_account)
    return new_account
    
    
def generate_account_number():
    account_number= ''
    raw_number="0123456789"
    for _ in range (10):
        account_number += random.choice(raw_number)
    return(account_number)

def display_menu():
    print("Welcome to FCMB ATM")
    print("1:Creat an Account")
    print("2:Check Balance")
    print("3: Withdraw")
    print("4: Exit")

def atm_menu():
    account= None
    while True:
        display_menu()
        choice = input("Select an option: ")
        if choice == "1":
            print("Fill the following")
            account=account_storage()
            #account_details()
            #account_storage()
               
        elif choice == "2":
            if account_list:
                print(f"Balance: {account.check_balance()}")
            else:
                print("No account found")
        elif choice == "3":
            amount = float(input("Enter the amount to withdraw: "))
            if account.withdraw(amount):
                print(f"Withdrew {amount} from your account.")
            else:
                print("Insufficient funds.")
    
        elif choice == "4":
            break

if __name__ == "__main__":
    account = generate_account_number()
    atm_menu()