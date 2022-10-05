# John Logiudice
# WA # 6 - Write a program for currency exchange / conversion.

import csv  # csv Library to load and save exchange rate data
import math
from time import sleep

# Constant for rate file name
RATE_FILE = 'conversion_rates.csv'


# Get and confirm a Y of N answer
def get_yn():
    # Loop until valid response is given
    while True:
        response = input("Please enter (Y)es or (N)o: ").lower()

        # Allow first letter or whole word
        if response in ('y', 'yes', '(y)es'):
            return 'y'
        elif response in ('n', 'no', '(n)o'):
            return 'n'


# Get text input
def get_text(f_input_msg):
    print(f"{f_input_msg}: ")
    while True:
        response = input('> ').upper()
        # If user enters no response
        if len(response) == 0:
            return None
        else:
            return response


# Check if string can be converted to float
def is_float(f_string):
    try:
        float(f_string.strip())
        return True
    except ValueError:
        return False


# Load rates from CSV file
# list[dictionary{}] format is:
#   f_rate_list = {'country': row['country'], 'currency': row['currency'], 'rate': row['rate']}
def load_rates(f_rate_file):
    # Attempt to open and read data file
    try:
        with open(f_rate_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            # initialize rate list
            f_rate_list = list()
            for row in reader:
                f_rate_list.append({'country': row['country'], 'currency': row['currency'], 'rate': row['rate']})

    # If file not found
    except FileNotFoundError:
        print()
        print("Error: File Not Found\n"
              f"The file '{f_rate_file}' could not be found. Please ensure it is in the\n"
              "application folder.")
        print()
        input("Press <enter> to quit.")
        quit()

    # If header of data file does not have correct field names
    except KeyError:
        print()
        print("Error: Incorrect header in data file\n"
              f"The data file '{f_rate_file}' does not have the correct header row.\n"
              "The first row must contain the names: country, currency, rate.")
        print()
        input("Press <enter> to quit.")
        quit()

    return f_rate_list


# Save rates to CSV file
def save_rates(f_rate_file, f_rate_list):
    # Attempt to open and read data file
    try:
        with open(f_rate_file, 'w', newline='') as csvfile:
            field_names = ('country', 'currency', 'rate')
            writer = csv.DictWriter(csvfile, field_names)
            writer.writeheader()
            for row in f_rate_list:
                writer.writerow(row)

    # If file not found
    except FileNotFoundError:
        print()
        print("Error: File Not Found\n"
              f"The file '{f_rate_file}' could not be found. Please ensure it is in the\n"
              "application folder.")
        print()
        input("Press <enter> to quit.")
        quit()

    # If header of data file does not have correct field names
    except KeyError:
        print()
        print("Error: Incorrect header in data file\n"
              f"The data file '{f_rate_file}' does not have the correct header row.\n"
              "The first row must contain the names: country, currency, rate.")
        print()
        input("Press <enter> to quit.")
        quit()

    return f_rate_list


# Get details of a currency
def currency_detail(f_order, f_rate_list):
    currency = f_rate_list[f_order]['currency']
    country = f_rate_list[f_order]['country']
    rate = f_rate_list[f_order]['rate']
    # Increase display order by 1 so list starts with 1, not 0
    return str(f_order+1), currency, country, rate


# Print the currency detail header
def print_currency_header():
    print('#   ' + 'Currency Name' + " " * 2 + 'Country' + " " * 11 + 'Rate', end='')


# Print one currency's details
def display_currency(f_order, f_rate_list):
    f_order_str, f_currency, f_country, f_rate = currency_detail(f_order, f_rate_list)

    f_order_str = f_order_str + ". "
    print(f_order_str, end='')
    print(" " * (4 - len(f_order_str)), end='')
    print(f_currency, end='')
    print(" " * (15 - len(f_currency)), end='')
    print(f_country, end='')
    print(" " * (18 - len(f_country)), end='')
    print(f_rate, end='')


# print the single rate details
def print_single_rate(f_update_currency, f_rate_list):
    print_currency_header()
    print()
    print('-' * 43)
    display_currency(f_update_currency, f_rate_list)


# Print current rates
def print_rates(f_rate_list):

    # List is printed in two columns
    list_len = len(f_rate_list)

    # To get the number of entries to print on the left side divide
    # list length in half but always have the greater number of
    # entries on the left side
    # math.ceil returns an integer rounded up
    half_list_len = math.ceil(list_len / 2)

    # Heading
    print_currency_header()
    print(" "*10, end='')
    print_currency_header()
    print()
    print('-'*43, end='')
    print(" "*8, end='')
    print('-'*43)

    for i in range(0, half_list_len):
        # Print left side list
        display_currency(i, f_rate_list)
        i2 = i + half_list_len
        if i2 < list_len:
            print(" " * (14 - len(f_rate_list[i]['rate'])), end='')
            display_currency(i2, f_rate_list)
            print()
        else:
            # Filler for no right entry
            print()
    print()


# Print main menu
def display_menu(f_menu_tuple):
    print("- - - - Menu - - - -")
    for i in range(0, len(f_menu_tuple)):
        print(f"{str(i+1)}. {f_menu_tuple[i]}")

    print()


# Get main menu response
def get_menu_response(f_menu_tuple):
    # loop until user gives valid menu response
    while True:
        # Ask user for menu number
        response = input("Enter the number of your menu choice: ").strip()
        # Check if response string is an integer
        if response.isdigit():
            # Check if response is a valid menu integer
            if (int(response) - 1) in range(0, len(f_menu_tuple)):
                return int(response)

        # User did not enter valid integer response
        print(f"Please enter a menu choice between 1 and {len(f_menu_tuple)}.")
        print()


# Get new rate
def get_rate():
    # loop until valid response or exit
    while True:
        response = input("Please enter the new rate (blank for no change): ").strip()
        # User entered nothing, return original amount
        if len(response) == 0:
            return None
        else:
            if not is_float(response):
                print("Please enter a valid numeric rate.")
            else:
                response = float(response)
                if response <= 0:
                    print("Please enter an amount greater than zero.")
                else:
                    # Convert rate to string rounded to 4 digits
                    response = str(round(response, 4))
                    return response


# Get and validate new conversion fee
def get_new_fee():
    # loop until valid response or exit
    while True:
        response = input("Please enter the new fee as a percent (blank for no change): ").strip()
        # User entered nothing
        if len(response) == 0:
            return None
        # Check if response ends with % sign
        elif not response.endswith('%'):
            print("Please enter a percentage ending with %.")
        else:
            response = response.rstrip('%')
            # Check if response can be converted to a float
            if not is_float(response):
                print("Please enter a valid number ending with %.")
            else:
                response = float(response)
                # Check if float value is between 0 and 100
                if response < 0 or response > 100:
                    print("Please enter a percent value between 0% and 100%.")
                else:
                    return response / 100


# Check that user selected currency type is valid
def get_currency_type(f_rate_list, f_input_msg):
    # loop until user selects valid currency type
    while True:
        # Get user input with message supplied
        print()
        response = input(f"{f_input_msg}: ").strip().rstrip('.')
        # If user enters no response
        if len(response) == 0:
            return None

        # check if an integer was entered
        elif response.isdigit():
            response = int(response)
            if response in range(1, len(f_rate_list)+1):
                return response

        # User did not enter a valid menu response
        print("Please enter a valid # from the currency list")


# Get the amount of currency to convert
def get_currency_amount(f_currency, f_country):
    # Loop until valid response is entered
    while True:
        print()
        response = input(f"Please enter the amount of {f_currency} {f_country} to convert (blank to cancel): ").strip()
        # If user enters no response
        if len(response) == 0:
            return None

        # If response can be converted to float
        elif is_float(response):
            response = float(response)

            if response > 0:
                return response

        # User did not enter a valid response
        print("Please enter a numeric currency amount greater than zero.")


# Convert currency based on from rate, to rate, and from amount
def currency_convert(f_from_rate, f_to_rate, f_amount, f_fee):
    # convert rate strings to float
    f_from_rate = float(f_from_rate)
    f_to_rate = float(f_to_rate)

    # Divide from currency by to currency to get rate, handle divide by zero
    try:
        exchange_rate = f_to_rate / f_from_rate
    except ZeroDivisionError:
        print('Error in conversion rate. Cannot divide by zero')
        return 0, 0

    # Multiply rate by exchange amount to get subtotal
    sub_total = exchange_rate * f_amount
    sub_total = round(sub_total, 4)

    # Multiply subtotal by fee percent to get fee
    fee = sub_total * f_fee
    fee = round(fee, 4)

    return sub_total, fee


# Menu for exchange rate actions
def exchange_menu(f_rate_list):
    # Loop to return to exchange rate menu until user exits
    while True:
        print()
        print("- - - - - Exchange rate Maintenance - - - - -")
        print()
        display_menu(exchange_menu_tuple)
        exchange_menu_response = get_menu_response(exchange_menu_tuple)
        exit_function, f_rate_list = exchange_action(exchange_menu_response, f_rate_list)

        if exit_function:
            return f_rate_list


# Perform exchange actions
def exchange_action(f_menu_choice, f_rate_list):

    # 1. Show exchange rates
    if f_menu_choice == 1:
        print()
        # Print rate list
        print_rates(f_rate_list)

    # 2. Change exchange rate
    if f_menu_choice == 2:
        print()
        # Print rate list
        print_rates(f_rate_list)

        # Get currency to update
        update_currency = get_currency_type(f_rate_list,
                                            "Please enter the # of the currency to update (Blank for no change)")

        if update_currency:
            # realign user input to list index
            update_currency -= 1
            print()

            # print the single rate details
            print_single_rate(update_currency, f_rate_list)
            print()

            # Get new rate from user
            print()
            new_rate = get_rate()
            print()
            if new_rate:
                print(f"The new rate is {new_rate}. Please confirm updating the rate table.")

                # User replied Yes - change rate
                if get_yn() == 'y':
                    f_rate_list[update_currency]['rate'] = new_rate
                    print()
                    print(f"rate for {f_rate_list[update_currency]['country']} "
                          f"{f_rate_list[update_currency]['currency']} " 
                          f"updated to {f_rate_list[update_currency]['rate']}.")

                # User replied No - no rate change
                else:
                    print()
                    print(f"rate change for {f_rate_list[update_currency]['country']} "
                          f"{f_rate_list[update_currency]['currency']} was canceled.")

        print("No rate change was made.")

    # 3. Add new currency
    if f_menu_choice == 3:
        print()

        # Get currency details
        new_currency_country = get_text("Enter the country name of this currency (blank to cancel)")
        # Loop will exit if user gives blank entry
        while True:
            if new_currency_country:
                new_currency_name = get_text("Enter the name of the new currency (blank to cancel)")

                if new_currency_name:
                    new_rate = get_rate()

                    if new_rate:
                        print(f"The new currency is: {new_currency_country} {new_currency_name} {new_rate}.")
                        print()
                        print("Please confirm updating the rate table.")

                        # User replied Yes - Add rate
                        if get_yn() == 'y':
                            f_rate_list.append({'country': new_currency_country, 'currency': new_currency_name,
                                                'rate': new_rate})
                            print()
                            print(f"rate for {new_currency_country} {new_currency_name} "
                                  f"added with rate {new_rate}.")

                        # User replied No - cancel rate add
                        else:
                            print()
                            print(f"New currency for {new_currency_country} {new_currency_name} was canceled.")
                        break

            print("No new currency was added.")
            break

    # 4. Remove currency
    if f_menu_choice == 4:
        print()
        # Print rate list
        print_rates(f_rate_list)

        # Get currency to remove
        remove_currency = get_currency_type(f_rate_list, "Please enter the # of the currency to remove (blank to cancel)")

        if remove_currency:
            # realign user input to list index
            remove_currency -= 1
            print()
            # print the single rate details
            print_single_rate(remove_currency, f_rate_list)

            print()
            print()
            # Get user confirm to remove currency
            print("Please confirm removing the currency and rate.")

            print()
            # User replied Yes - Add rate
            if get_yn() == 'y':
                print()
                print(f"rate for {f_rate_list[remove_currency]['country']} "
                      f"{f_rate_list[remove_currency]['currency']} has been removed from the list.")

                del f_rate_list[remove_currency]

            # User replied No - cancel rate add
            else:
                print()
                print(f"Removing currency {f_rate_list[remove_currency]['country']} "
                      f"{f_rate_list[remove_currency]['currency']} was canceled.")

        else:
            print()
            print("Remove a currency was cancelled.")

    # 5. Save rates to file
    if f_menu_choice == 5:
        print()

        print("Are you sure you want to save loaded rates to the file?")
        print("--------- WARNING ---------")
        print("The existing rate file will be overwritten.")
        print()

        # User responded Yes - Save rates to csv file
        if get_yn() == 'y':
            print()
            print("The new rates have been written to the file.")
            save_rates(RATE_FILE, f_rate_list)
        # User responded No - Do not save rates to file
        else:
            print()
            print("The rate file has not been changed.")

    # 6. Load rates from file
    if f_menu_choice == 6:
        print()

        print("Are you sure you want to reload rates from the file?")
        print("--------- WARNING ---------")
        print("The existing loaded rates will be overwritten.")
        print()

        # User responded Yes - Load rates from file
        if get_yn() == 'y':
            print()
            print("The rates have been reloaded from the file.")
            # Load rates into dictionary from file
            f_rate_list = load_rates(RATE_FILE)
        # User responded No - Do not reload rates from file
        else:
            print()
            print("Operation canceled. Rates were not loaded from file.")

    # 7. Exit - Return to main menu
    if f_menu_choice == 7:
        return True, f_rate_list

    return False, f_rate_list


# Perform main menu action
def main_action(f_menu_choice, f_conv_fee, f_rate_list):

    # 1. Show exchange rates
    if f_menu_choice == 1:
        # Print rates
        print()
        print_rates(f_rate_list)

        # Current exchange fee as percentage
        print("Exchange fee: " + "{:.2%}".format(f_conv_fee))
        print()

    # 2. Set exchange fee
    elif f_menu_choice == 2:
        print()
        print("Exchange fee is a percentage of the final conversion amount.")
        print("Current exchange fee: " + "{:.2%}".format(f_conv_fee))
        print()
        new_fee = get_new_fee()
        print()
        # if user entered a new rate
        if new_fee:
            f_conv_fee = new_fee
            print("The new conversion fee is " + "{:.2%}".format(f_conv_fee))
        # User did not enter a new rate
        else:
            print("The conversion fee of " + "{:.2%}".format(f_conv_fee) + " was not changed.")

    # 3. Convert a currency
    elif f_menu_choice == 3:
        print()
        print("currency Conversion")
        # Print current rates
        print_rates(f_rate_list)

        # Get the FROM currency type
        from_currency = get_currency_type(f_rate_list,
                                          "Please enter the # of the currency to convert FROM (blank to cancel)")

        # verify response was entered, loop will exit if no entry
        while True:
            if from_currency:
                # Realign user input to list index
                from_currency -= 1
                # Get the FROM currency amount
                exchange_amount = get_currency_amount(f_rate_list[from_currency]['country'],
                                                      f_rate_list[from_currency]['currency'])

                if exchange_amount:
                    # get the TO currency type
                    to_currency = get_currency_type(f_rate_list,
                                                    "Please enter the # of the currency to convert TO (blank to cancel)")

                    if to_currency:
                        # Realign user input to list index
                        to_currency -= 1
                        # Do conversion math
                        converted_amount, fee = currency_convert(f_rate_list[from_currency]['rate'],
                                                                 f_rate_list[to_currency]['rate'],
                                                                 exchange_amount, conversion_fee)

                        print()
                        # Sleep delay gives illusion that calculation work takes some time
                        sleep(.6)
                        print(f"You can exchange {exchange_amount} {f_rate_list[from_currency]['country']} "
                              f"{f_rate_list[from_currency]['currency']} for {converted_amount} "
                              f"{f_rate_list[to_currency]['country']} {f_rate_list[to_currency]['currency']}.")
                        print(f"The exchange fee is {fee} {f_rate_list[to_currency]['currency']}.")
                        print(f"The final converted amount with fee is {round(converted_amount - fee, 4)}"
                              f" {f_rate_list[to_currency]['country']} {f_rate_list[to_currency]['currency']}.")
                        print()
                        input("Press <enter> to continue.")
                        break

            # User canceled by giving no entry
            print()
            print("Conversion was cancelled.")
            break

    # 4. Update exchange rates
    elif f_menu_choice == 4:
        f_rate_list = exchange_menu(f_rate_list)

    # 5. Quit
    elif f_menu_choice == 5:
        return True, f_conv_fee, f_rate_list

    return False, f_conv_fee, f_rate_list


# Main
# Set default conversion fee
conversion_fee = 0.01

# Load rates into dictionary from file
rate_list = load_rates(RATE_FILE)

# Menu options
main_menu_tuple = ('Show exchange rates', 'Set exchange fee', 'Convert a currency',
                   'Update exchange rates', 'Quit')

exchange_menu_tuple = ('Show exchange rates', 'Change exchange rate', 'Add new currency',
                       'Remove a currency', 'Save rates to file', 'Load rates from file',
                       'Return to Main Menu')

# intro
print("- - - - - Conversion Utility - - - - -")
print("This program will help you convert currency")
print("")  # extra blank line

# Print rates
print_rates(rate_list)

# Current exchange fee as percentage
print("Exchange fee: " + "{:.2%}".format(conversion_fee))
print()

while True:
    print()
    display_menu(main_menu_tuple)
    # get input from user

    menu_response = get_menu_response(main_menu_tuple)

    quit_program, conversion_fee, rate_list = main_action(menu_response, conversion_fee, rate_list)

    if quit_program:
        print()
        print("Thank you for using the Conversion Utility.")
        print()
        input("Press <enter> to quit.")
        quit()

    print()
