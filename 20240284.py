accounts = []



def exit_menu(input_val):
    if input_val.lower() == "exit":
        return True
    return False


def has_only_alphabets(text):
    return text.isalpha()


def main_menu():
    print("".center(150, '-'))
    print("ABC Bank".center(150))
    print("Main Menu".center(150))
    print("\n")
    print("1) Add a new customer")
    print("2) View details of a customer including his/her bank balance")
    print("3) View details of all the customers with their bank balances")
    print("4) Deposit money to a given account")
    print("5) Withdraw money from a given account")
    print("6) Update Customer Details")
    print("7) Exit")
    next_choice = input("Your Choice : ".rjust(150))
    return next_choice


def save_details(bank_acc_num, nic, first_name, last_name, date, permanent_address, phone_number, bank_balance):
    acc_list = [bank_acc_num, nic, first_name, last_name, date, permanent_address, phone_number, bank_balance]
    accounts.append(acc_list)
    print("\nAccount saved successfully!\n")


def date_validation(date):
    try:
        day, month, year = map(int, date.split('/'))
        if year < 1903 or year > 2024:
            return False
        days_in_month_30 = [4, 6, 9, 11]
        days_in_month_31 = [1, 3, 5, 7, 8, 10, 12]

        if month < 1 or month > 12:
            return False

        if month in days_in_month_30 and day > 30:
            return False

        if month in days_in_month_31 and day > 31:
            return False

        if month == 2:
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        if day > 29:
                            return False
                    else:
                        if day > 28:
                            return False
                else:
                    if day > 29:
                        return False
            else:
                if day > 28:
                    return False
        return True
    except ValueError:
        return False


def phone_number_format(number):
    number = str(number)
    if len(number) > 5:
        if number[:3] == "+94":
            number = number[3:]
        elif number[:5] == "(+94)":
            number = number[5:]
        elif number[:2] == "94":
            number = number[2:]
        elif number[0] == "0":
            number = number[1:]
    return number


def nic_check(nic_input):
    for account in accounts:
        if account[1] == nic_input:
            return False
    return True


def input_with_exit(prompt):
    user_input = input(prompt)
    if exit_menu(user_input):
        return None
    return user_input


def adding_customer():
    print("".center(150, '-'))
    print("ABC Bank".center(150))
    if len(accounts)>=5:
        print("Maxmum account count reached, only 5 accounts can be created.")
        return 0;
    print("Add a new customer".center(150))
    print(
        "Please enter 'exit' if you want to access the main menu again, remember the current entry will be lost in this case.")
    print("\n")
    bank_acc_num = f"123569046{len(accounts)}"
    print("Bank account number  - ", bank_acc_num)

    nic = input_with_exit("NIC - ")
    if nic is None:
        return 0

    while not (len(str(nic)) == 10 and nic[:-1].isdigit() and nic[-1].upper() in ['V', 'X'] and nic_check(nic)):
        print("Error! A valid NIC should be exactly 10 characters long, with the last character being 'V' or 'X'")
        nic = input_with_exit("NIC - ")
        if nic is None:
            return 0
    nic = str(nic.upper())

    first_name = input_with_exit("First Name - ")
    if first_name is None:
        return 0
    while not has_only_alphabets(first_name) or not (1 <= len(first_name) <= 10):
        print("Error! First name should be a string with 1 to 10 characters")
        first_name = input_with_exit("First Name - ")
        if first_name is None:
            return 0
    first_name = first_name.capitalize()

    last_name = input_with_exit("Last Name - ")
    if last_name is None:
        return 0
    while not has_only_alphabets(last_name) or not (1 <= len(last_name) <= 15):
        print("Error! Last name should be a string with 1 to 15 characters")
        last_name = input_with_exit("Last Name - ")
        if last_name is None:
            return 0
    last_name = last_name.capitalize()

    date = input_with_exit("Birth Date (DD/MM/YYYY) - ")
    if date is None:
        return 0
    while not date_validation(date):
        print("Error! Invalid birth date")
        date = input_with_exit("Birth Date (DD/MM/YYYY) - ")
        if date is None:
            return 0

    permanent_address = input_with_exit("Permanent Address - ")
    if permanent_address is None:
        return 0
    while not (1 <= len(permanent_address) <= 15):
        print("Error! Permanent address should be a string with a maximum of 15 characters")
        permanent_address = input_with_exit("Permanent Address - ")
        if permanent_address is None:
            return 0

    phone_number = input_with_exit("Phone Number - (+94) ")
    if phone_number is None:
        return 0
    phone_number = phone_number_format(phone_number)
    while not (len(phone_number) == 9 and phone_number.isdigit() and phone_number[0] != "0"):
        print("Error! Phone number should be a 9-digit number after the country code")
        phone_number = input_with_exit("Phone Number - (+94) ")
        if phone_number is None:
            return 0
    phone_number = f"(+94) {phone_number}"

    bank_balance = "99999.99"
    save = input_with_exit("Do you want to save the account (Yes / No)? ").lower()
    if save is None:
        return 0
    while save not in ["yes", "no"]:
        print("Invalid Input. Please enter 'yes' or 'no'.")
        save = input_with_exit("Do you want to save the account (Yes / No)? ").lower()
        if save is None:
            return 0
    if save == "yes":
        save_details(bank_acc_num, nic, first_name, last_name, date, permanent_address, phone_number, bank_balance)
    else:
        save = input_with_exit(
            "Are you sure that you do not want to save the account (save - Yes / don't - No)? ").lower()
        if save is None:
            return 0
        while save not in ["yes", "no"]:
            print("Invalid Input. Please enter 'yes' or 'no'.")
            save = input_with_exit(
                "Are you sure that you do not want to save the account (save - Yes / don't - No)? ").lower()
            if save is None:
                return 0
        if save == "yes":
            save_details(bank_acc_num, nic, first_name, last_name, date, permanent_address, phone_number, bank_balance)
        else:
            print("\nAccount not saved.\n")
    return 0


def view_customer():
    print("".center(150, '-'))
    print("ABC Bank".center(150))
    print("View details of a customer.".center(150))
    print("\n")
    acc_number = input_with_exit("Enter the account number of the customer: ")
    if acc_number is None:
        return 0
    while not acc_number.isdigit() or len(acc_number) != 10:
        print("Invalid account number. Please enter a 10-digit account number.")
        acc_number = input_with_exit("Enter the account number of the customer: ")
        if acc_number is None:
            return 0

    found = False
    for account in accounts:
        if account[0] == acc_number:
            found = True
            print("\nCustomer Details:\n")
            print(f"Account Number: {account[0]}")
            print(f"NIC: {account[1]}")
            print(f"Name: {account[2]} {account[3]}")
            print(f"Birth Date: {account[4]}")
            print(f"Permanent Address: {account[5]}")
            print(f"Phone Number: {account[6]}")
            print(f"Bank Balance: {account[7]}")
            break
    if not found:
        print("\nAccount number not found.\n")
    return 0


def view_all_customers():
    print(f"".center(150, "-"))
    print(f"ABC Bank".center(150))
    print(f"View Details of All Customers\n".center(150))
    print(f"{'NIC Number'.center(20):<20}{'Account Number'.center(20):<20}{'First Name'.center(20):<20}"
          f"{'Last Name'.center(20):<20}{'Bank Balance'.center(20):<20}\n".center(150))
    for account in accounts:
        bank_balance = f"{float(account[7]):.2f}"
        print(
            f"{account[1].center(20):<20}{account[0].center(20):<20}{account[2].center(20):<20}{account[3].center(20):<20}{bank_balance.center(20):<20}\n".center(
                150))
    next_step = input("Do you want to update the account details (Yes/No)? ")
    while next_step.lower() not in ['yes', 'no']:
        print(f"Invalid choice. Please enter 'Yes' or 'No'.")
        next_step = input("Do you want to update the account details (Yes/No)? ")

    if next_step.lower() == 'yes':
        print(f"".center(150, "-"))
        print(f"ABC Bank".center(150))
        print(f"Update Customer Details".center(150))
        update_customer_details()
    elif next_step.lower() == 'no':
        return
    return 0


def deposit_money():
    print("".center(150, '-'))
    print("ABC Bank".center(150))
    print("Deposit Money".center(150))
    print("\n")
    acc_number = input_with_exit("Enter the account number of the customer: ")
    if acc_number is None:
        return 0
    while not acc_number.isdigit() or len(acc_number) != 10:
        print("Invalid account number. Please enter a 10-digit account number.")
        acc_number = input_with_exit("Enter the account number of the customer: ")
        if acc_number is None:
            return 0

    found = False
    for account in accounts:
        if account[0] == acc_number:
            found = True
            deposit_amount = input_with_exit("Enter the amount to deposit: ")
            if deposit_amount is None:
                return 0
            while not deposit_amount.replace('.', '', 1).isdigit() or float(deposit_amount) <= 0:
                print("Invalid amount. Please enter a positive number.")
                deposit_amount = input_with_exit("Enter the amount to deposit: ")
                if deposit_amount is None:
                    return 0
            deposit_amount = float(deposit_amount)
            account[7] = f"{float(account[7]) + deposit_amount:.2f}"
            print(f"\n{deposit_amount:.2f} has been deposited to account {acc_number}. New balance: {account[7]}\n")
            break
    if not found:
        print("\nAccount number not found.\n")
    return 0


def withdraw_money():
    print("".center(150, '-'))
    print("ABC Bank".center(150))
    print("Withdraw Money".center(150))
    print("\n")
    acc_number = input_with_exit("Enter the account number of the customer: ")
    if acc_number is None:
        return 0
    while not acc_number.isdigit() or len(acc_number) != 10:
        print("Invalid account number. Please enter a 10-digit account number.")
        acc_number = input_with_exit("Enter the account number of the customer: ")
        if acc_number is None:
            return 0

    found = False
    for account in accounts:
        if account[0] == acc_number:
            found = True
            withdraw_amount = input_with_exit("Enter the amount to withdraw: ")
            if withdraw_amount is None:
                return 0
            while not withdraw_amount.replace('.', '', 1).isdigit() or float(withdraw_amount) <= 0 or float(
                    withdraw_amount) > float(account[7]):
                print("Invalid amount. Please enter a positive number less than or equal to the account balance.")
                withdraw_amount = input_with_exit("Enter the amount to withdraw: ")
                if withdraw_amount is None:
                    return 0
            withdraw_amount = float(withdraw_amount)
            account[7] = f"{float(account[7]) - withdraw_amount:.2f}"
            print(f"\n{withdraw_amount:.2f} has been withdrawn from account {acc_number}. New balance: {account[7]}\n")
            break
    if not found:
        print("\nAccount number not found.\n")
    return 0


def update_customer_details():
    print("".center(150, '-'))
    print("ABC Bank".center(150))
    print("Update Customer Details".center(150))
    print("\n")
    acc_number = input_with_exit("Enter the account number of the customer: ")
    if acc_number is None:
        return 0
    while not acc_number.isdigit() or len(acc_number) != 10:
        print("Invalid account number. Please enter a 10-digit account number.")
        acc_number = input_with_exit("Enter the account number of the customer: ")
        if acc_number is None:
            return 0

    found = False
    for account in accounts:
        if account[0] == acc_number:
            found = True
            print("Enter new details (leave blank to keep current value):")
##            new_NIC = input_with_exit(f"NIC ({account[1]}): ")
##            if new_NIC == None :
##                new_NIC = account[1]
##            else:
##                while not (len(str(new_NIC)) == 10 and new_NIC[:-1].isdigit() and new_NIC[-1].upper() in ['V', 'X'] and nic_check(new_NIC)):
##                    print("Error! A valid NIC should be exactly 10 characters long, with the last character being 'V' or 'X'")
##                    new_NIC = input_with_exit(f"NIC ({account[1]}): ") or account[1]
##                    if new_NIC ==None :
##                        new_NIC = account[1]
##                new_NIC = str(nic.upper())
            new_first_name = new_first_name.capitalize()
            new_first_name = input_with_exit(f"First Name ({account[2]}): ") or account[2]
            while not has_only_alphabets(new_first_name) or not (1 <= len(new_first_name) <= 10):
                print("Error! First name should be a string with 1 to 10 characters")
                new_first_name = input_with_exit(f"First Name ({account[2]}): ") or account[2]
            new_first_name = new_first_name.capitalize()

            new_last_name = input_with_exit(f"Last Name ({account[3]}): ") or account[3]
            while not has_only_alphabets(new_last_name) or not (1 <= len(new_last_name) <= 15):
                print("Error! Last name should be a string with 1 to 15 characters")
                new_last_name = input_with_exit(f"Last Name ({account[3]}): ") or account[3]
            new_last_name = new_last_name.capitalize()

            new_date = input_with_exit(f"Birth Date ({account[4]}) (DD/MM/YYYY): ") or account[4]
            while not date_validation(new_date):
                print("Error! Invalid birth date")
                new_date = input_with_exit(f"Birth Date ({account[4]}) (DD/MM/YYYY): ") or account[4]

            new_address = input_with_exit(f"Permanent Address ({account[5]}): ") or account[5]
            while not (1 <= len(new_address) <= 15):
                print("Error! Permanent address should be a string with a maximum of 15 characters")
                new_address = input_with_exit(f"Permanent Address ({account[5]}): ") or account[5]

            new_phone_number = input(f"Phone Number ({account[6]}) :(+94) ")
            if new_phone_number ==None :
                new_phone_number = account[6]
            else:
                new_phone_number = phone_number_format(new_phone_number)
                while not (len(new_phone_number) == 9 and new_phone_number.isdigit() and new_phone_number[0] != "0"):
                    print("Error! Phone number should be a 9-digit number after the country code")
                    new_phone_number = input(f"Phone Number ({account[6]}) :(+94) ") or account[6]
                    if new_phone_number ==None :
                        new_phone_number = account[6]
                new_phone_number = f"(+94) {new_phone_number}"
            save=input_with_exit("Do you want to save the details (yes/ no) ?")
            save=save.lower()
            while not(save=="yes" or save=="no"):
                print("Invalid input. Please enter 'yes' or 'no'.")
                save=input_with_exit("Do you want to save the details (yes/ no) ?")
            if save=="yes":
                account[1] = new_NIC 
                account[2] = new_first_name
                account[3] = new_last_name
                account[4] = new_date
                account[5] = new_address
                account[6] = new_phone_number
                print("\nCustomer details updated successfully!\n")
            else:
                print("\nCustomer details are not updated!\n")
    if not found:
        print("\nAccount number not found.\n")
    return 0
def exit_program():
    print("".center(100, "-"))
    print("                                         ABC Bank")
    print("\n")
    exit=input_with_exit("Are you sure that you want to exit (Yes/ no)?")
    exit=exit.lower()
    while not (exit=="yes" or exit=="no"):
        print("Invalid Input.Please enter 'yes' or 'no'.")
        exit = input_with_exit("Are you sure that you want to exit (Yes/ no)?")
    if exit=="yes":
        print("Thank you for using ABC Bank. Goodbye!")
        return None
    else:
        return 0

while True:
    choice = main_menu()
    if choice == "1":
        adding_customer()
    elif choice == "2":
        view_customer()
    elif choice == "3":
        view_all_customers()
    elif choice == "4":
        deposit_money()
    elif choice == "5":
        withdraw_money()
    elif choice == "6":
        update_customer_details()
    elif choice == "7":
        exit_program()
        break
    else:
        print("Invalid choice. Please try again.")
