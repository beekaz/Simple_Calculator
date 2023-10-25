from atm import account_details, atm_menu, generate_account_number

def main():
    print("Welcome to FCMB ATM")
    user_account = account_details()
    atm_menu(user_account)

if __name__ == "__main__":
    main()