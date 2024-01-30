'''
SafeBank app
- Checking Balances
- Transferring Funds
- Depositing Money
- Withdrawing Money
'''

import random as rd

#Creates a current account with a random amount in it.
current_balance = rd.randint(10, 9999)
'''savings account variable that can be changed if the user chooses 
to transfer any funds to it.'''
savings_balance = 0

def pin_validation():
    '''A function to confirm the user's PIN'''
    pin_check_counter = 0
    while True:
        confirm_pin = input("Please can you confirm your PIN : ")
        if confirm_pin == user_pin:
            break
        if confirm_pin != user_pin and pin_check_counter == 0:
            pin_check_counter += 1
            print("Incorrect PIN. 2 Attempts Remaining!")
            continue
        if confirm_pin != user_pin and pin_check_counter == 1:
            pin_check_counter += 1
            print("Incorrect PIN. 1 Attempt Remaining!")
            continue
        if confirm_pin != user_pin and pin_check_counter == 2:
            print('''Maximium number of attempts reached.''')
            break
    return confirm_pin

def transfer_funds():
    '''A function to transfer funds'''
    print('''
You have selected to transfer funds to your savings account.
''')
    print(f"Current Account: £{current_balance}")
    while True:
        saving_acc_transfer = input('''
Please enter the amount you wish to transfer to your saving account : £''')
        try:
            saving_acc_transfer = int(saving_acc_transfer)
            break
        except ValueError:
            print('''
Invalid amount. Please only enter the amount you wish to transfer.''')
    if saving_acc_transfer > current_balance:
        print('''
You have insufficent funds to carry out this transfer of funds.''')
        return 0
    print(f'''
You wish to transfer £{saving_acc_transfer} into your savings account.''')
    while True:
        transfer_conf = input("Please confirm with Yes or No (Y/N) : ")
        transfer_conf = transfer_conf.lower()
        if transfer_conf in {"y","yes"}:
            print("Transfer Confirmed!")
            return saving_acc_transfer
        if transfer_conf in {"n", "no"}:
            print("Transfer Cancelled!")
            return 0
        print("Invalid input. Please confirm with Y or N.")

def deposit_funds():
    '''A function to deposit funds into account'''
    print('''
You have selected to desposit some funds into your current account.''')
    while True:
        current_acc_deposit = input('''
Please enter the amount you wish to deposit to your current account : £''')
        try:
            current_acc_deposit = int(current_acc_deposit)
            break
        except ValueError:
            print('''
Invalid amount. Please only enter the amount you wish to deposit.''')
    while True:
        desposit_conf = input("Please confirm with Yes or No (Y/N) : ")
        desposit_conf = desposit_conf.lower()
        if desposit_conf in {"y","yes"}:
            print("Deposit Confirmed!")
            return current_acc_deposit
        if desposit_conf in {"n", "no"}:
            print("Deposit Cancelled!")
            return 0
        print("Invalid input. Please confirm with Y or N.")

def withdraw_funds():
    '''A function to withdraw funds into account'''
    print('''
You have selected to withdraw some funds into your current account.''')
    while True:
        current_acc_withdraw = input('''
Please enter the amount you wish to withdraw to your current account : £''')
        try:
            current_acc_withdraw = int(current_acc_withdraw)
            break
        except ValueError:
            print('''
Invalid amount. Please only enter the amount you wish to withdraw.''')
    if current_acc_withdraw > 100:
        print("Maximum withdrawals is £100. Please try again.")
        return 0
    while True:
        withdraw_conf = input("Please confirm with Yes or No (Y/N) : ")
        withdraw_conf = withdraw_conf.lower()
        if withdraw_conf in {"y","yes"}:
            print("Withdraw Confirmed!")
            return current_acc_withdraw
        if withdraw_conf in {"n", "no"}:
            print("Withdraw Cancelled!")
            return 0
        print("Invalid input. Please confirm with Y or N.")

print("Welcome to the SafeBank Banking App!\nPlease enter your details below.")

# Asks user to enter some credentials
while True:
    user_email = input("Please enter email address : ")

    if "@" in user_email and "." in user_email:
        print("Email Exists.")
        break
    print("Invalid Email, Please try again!")
    continue

while True:
    user_pin = input("Please enter your PIN : ")

    if len(user_pin) == 4 and user_pin.isdigit():
        print("User PIN Accepted.")
        break
    print("Invalid PIN, please try again.")
    continue

print("\nPlease make a selection from the options below : ")
while True:
    print('''
1 - To check your current balance.
2 - To transfer funds.
3 - To deposit some money into your current account.
4 - To withdraw from your current account.
5 - Exit''')
    user_choice = input('''
Please make your selection (enter a number from above) : ''')

    if user_choice == "1":
        if user_pin == pin_validation():
            print(f'''
Your current balance is £{current_balance}.''')
            continue
        print("Access Denied!")
        break
    if user_choice == "2":
        if user_pin == pin_validation():
            transfer_amount = transfer_funds()
            savings_balance += transfer_amount
            current_balance -= transfer_amount
            print(f'''
Your Account Balances:
Savings Account : £{savings_balance}.
Current Account : £{current_balance}.''')
            continue
    if user_choice == "3":
        if user_pin == pin_validation():
            deposit_amount = deposit_funds()
            current_balance += deposit_amount
            print(f'''
Your Current account now has £{current_balance}.''')
    if user_choice == "4":
        if user_pin == pin_validation():
            withdraw_amount = withdraw_funds()
            current_balance -= withdraw_amount
            print(f'''
You have withdrawn £{withdraw_amount}.
Your Current account now has £{current_balance}''')
    if user_choice == "5":
        print("Thank you for using SafeBank.")
        break
