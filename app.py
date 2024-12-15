from classes.bank import bank
from classes.account import account
# from classes import account as Account

banks = []

def format_username(user):
    formatted_username = user[0].upper()
    capitalize = False
    
    for char in user[1:]:
        if char == " ":
            capitalize = True
            formatted_username += char
            continue

        if capitalize:
            formatted_username += char.upper()
            capitalize = False
        else:
            formatted_username += char.lower()

    return formatted_username

def create_banks():
    banks.append(bank("TD", 15, 17)) # banks.append(bank("Toronto Dominion Bank", 15))
    banks.append(bank("RBC", 20, 18)) # banks.append(bank("Royal Bank of Canada", 20))
    banks.append(bank("CIBC", 10, 19)) # banks.append(bank("Canadian Imperial Bank of Commerce", 10))

def main():
    create_banks()

    for bank in banks:
        print(bank)

    valid_bank = False
    while not valid_bank:
        chosen_bank = input("Which bank would you like to open an account with today? ")     
        try:
            for bank in banks:
                if bank.name.lower().replace(' ', '') == chosen_bank.lower().replace(' ', ''):
                    valid_bank = True
                    chosen_bank = bank
                    break
        except:
            continue

    print("You have chosen to open an account with " + chosen_bank.name)
    
    user_name = ""
    while not user_name.replace(' ', '').isalpha() or 20 < len(user_name) < 2:
        try:
            user_name = input("Please enter your first and last name (2 to 20 characters max, only letters): ")
        except:
            continue    
    user_name = format_username(user_name)

    user_age = ""
    while not user_age.isnumeric():
        try:
            user_age = input("Please enter your age: ")
        except:
            continue

    user_age = int(user_age)
    if user_age < chosen_bank.minimumAgeRequirement:
        print(f"Sorry, you must be at least {chosen_bank.minimumAgeRequirement} years old to open an account with {chosen_bank.name}")
        return
    
    user_balance = ""
    while not user_balance.replace('.', '', 1).isdigit():
        try:
            user_balance = input("Please enter the amount you would like to initially deposit (example: 0.00): ")
        except:
            continue

    user_balance = float(user_balance)
    user_account = account(user_name, user_age, user_balance)
    chosen_bank.registerAccount(user_account)

    print(f"Successfully opened an account with {chosen_bank.name}.\nHere is your account information: {user_account}")
    print(chosen_bank)

main()