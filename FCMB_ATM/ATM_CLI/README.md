
#ATM CLI Program
This is a simple Command-Line Interface (CLI) program that simulates an ATM (Automated Teller Machine) for FCMB (First City Monument Bank). Users can create accounts, check balances and withdraw money.

##Features

###Create an account: Users can create a new bank account. An account number is generated, and the account is automatically funded with 1000 currency units upon creation.

###Check Balance: Users can check the current balance of their account.

###Withdraw: Users can withdraw funds from their account, provided they have sufficient balance.

####main.py: This file is the entry point of the program. It initializes the ATM and starts the main menu.

####account.py: This file defines the Account class, which represents a bank account. It includes methods for checking the balance, withdrawing, and transferring funds. The balance is automatically set to 1000 upon account creation.

####atm.py: This is the main program file. It includes functions for user input and the main ATM menu. Users can create accounts, check balances, withdraw, transfer funds, and exit the program. The program uses the Account class from account.py to manage bank accounts.