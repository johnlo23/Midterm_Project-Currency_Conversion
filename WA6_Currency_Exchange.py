# John Logiudice
# WA # 6 - Write a program for currency exchange / conversion.

import csv  # csv Library to load and save exchange rate data
import math

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
    print(f"{f_input_msg} :")
    while True:
        response = input('> ').upper()
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
def load_rates(rate_file):
    # Attempt to open and read data file
    try:
        with open(rate_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            # initialize rate list
            f_rate_list = list()
            for row in reader:
                f_rate_list.append({'country': row['COUNTRY'], 'currency': row['CURRENCY'], 'rate': row['RATE']})

    # If file not found
    except FileNotFoundError:
        print()
        print("Error: File Not Found\n"
              f"The file '{rate_file}' could not be found. Please ensure it is in the\n"
              "application folder.")
        print()
        input("Press <enter> to quit.")
        quit()

    # If header of data file does not have correct field names
    except KeyError:
        print()
        print("Error: Incorrect header in data file\n"
              f"The data file '{rate_file}' does not have the correct header row.\n"
              "The first row must contain the names: COUNTRY, CURRENCY, RATE.")
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
    print()
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
        print(f"Please enter a digit between 1 and {len(f_menu_tuple)}.")


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
def get_new_fee(f_conversion_fee):
    # loop until valid response or exit
    while True:
        response = input("Please enter the new fee as a percent (blank for no change): ").strip()
        # User entered nothing, return original amount
        if len(response) == 0:
            return f_conversion_fee
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
        # check if an integer was entered
        if response.isdigit():
            response = int(response)
            if response in range(1, len(f_rate_list)+1):
                # Decrease order by 1 to match list index
                return response - 1

        # User did not enter a valid menu response
        print("Please enter a valid # from the currency list")


# Get the amount of currency to convert
def get_currency_amount(f_currency, f_country):
    # Loop until valid response is entered
    while True:
        print()
        response = input(f"Please enter the amount of {f_currency} {f_country} to convert: ").strip()
        if is_float(response):
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
        exchange_rate = f_from_rate / f_to_rate
    except ZeroDivisionError:
        print('Error in conversion rate. Cannot divide by zero')
        return 0, 0

    # Multiply rate by exchange amount to get sub-total
    sub_total = exchange_rate * f_amount
    sub_total = round(sub_total, 4)

    # Multiply sub-total by fee percent to get fee
    fee = sub_total * f_fee
    fee = round(fee, 4)

    return sub_total, fee


# Menu for exchange rate actions
def exchange_menu(f_rate_list):
    # Loop to return to exchange rate menu until user exits
    while True:
        print()
        print("- - - - - Exchange Rate Maintenance - - - - -")
        print()
        display_menu(exchange_menu_tuple)
        exchange_menu_response = get_menu_response(exchange_menu_tuple)
        exchange_action(exchange_menu_response, f_rate_list)


# Perform exchange actions
def exchange_action(f_menu_choice, f_rate_list):

    # 1. Show exchange rates
    if f_menu_choice == 1:
        print_rates(f_rate_list)

    # 2. Change exchange rate
    if f_menu_choice == 2:
        print_rates(f_rate_list)
        update_currency = get_currency_type(f_rate_list, "Please enter the # of the currency to update")
        # print the single rate details
        print()
        print_currency_header()
        print()
        print('-' * 43)
        display_currency(update_currency, f_rate_list)
        print()
        new_rate = get_rate()
        print()
        if new_rate:
            print(f"The new rate is {new_rate}. Please confirm updating the rate table.")
            if get_yn() == 'y':
                f_rate_list[update_currency]['rate'] = new_rate
                print()
                print(f"Rate for {f_rate_list[update_currency]['country']} {f_rate_list[update_currency]['currency']} " 
                      f"updated to {f_rate_list[update_currency]['rate']}.")
            else:
                print()
                print(f"Rate change for {f_rate_list[update_currency]['country']} {f_rate_list[update_currency]['currency']} was canceled.")
        else:
            print("No rate change was made.")

    # 3. Add new currency
    if f_menu_choice == 3:
        print()
        print()
        new_currency_country = get_text("Enter the country name of this currency")

        while True:
            if new_currency_country:
                new_currency_name = get_text("Enter the name of the new currency")

                if new_currency_name:
                    new_rate = get_rate()

                    if new_rate:
                        print(f"The new rate is: {new_currency_country} {new_currency_name} {new_rate}. Please confirm updating the rate table.")
                        if get_yn() == 'y':
                            #f_rate_list[update_currency]['rate'] = new_rate
                            print()
                            print(
                                f"Rate for {new_currency_country} {new_currency_name} "
                                f"added with rate {new_rate}.")
                        else:
                            print()
                            print(
                                f"New currency for {new_currency_country} {new_currency_name} was canceled.")
                        break

            print("No rate change was made.")
            break





# Perform main menu action
def main_action(f_menu_choice, f_conv_fee, f_rate_list):

    # 1. Show exchange rates
    if f_menu_choice == 1:
        # Print rates
        print()
        print_rates(rate_list)

    # 2. Set exchange fee
    elif f_menu_choice == 2:
        print()
        print("Exchange fee is a percentage of final conversion amount.")
        print("Current exchange fee: " + "{:.2%}".format(f_conv_fee))
        f_conv_fee = get_new_fee(f_conv_fee)
        print()
        print("The new conversion fee is " + "{:.2%}".format(f_conv_fee))

    # 3. Convert a currency
    elif f_menu_choice == 3:
        print()
        print("Currency Conversion")
        # Print current rates
        print_rates(f_rate_list)

        # Get the FROM currency type
        from_currency = get_currency_type(f_rate_list, "Please enter the # of the currency to convert FROM")

        # Get the FROM currency amount
        exchange_amount = get_currency_amount(f_rate_list[from_currency]['country'],
                                              f_rate_list[from_currency]['currency'])

        # get the TO currency type
        to_currency = get_currency_type(f_rate_list, "Please enter the # of the currency to convert TO")

        # Do conversion math
        converted_amount, fee = currency_convert(f_rate_list[from_currency]['rate'],
                                                 f_rate_list[to_currency]['rate'],
                                                 exchange_amount, conversion_fee)

        print()
        print(f"You can exchange {exchange_amount} {f_rate_list[from_currency]['country']} "
              f"{f_rate_list[from_currency]['currency']} for {converted_amount} "
              f"{f_rate_list[to_currency]['country']} {f_rate_list[to_currency]['currency']}.")
        print(f"The exchange fee is {fee} {f_rate_list[to_currency]['currency']}.")
        print(f"The final converted amount with fee is {round(converted_amount - fee, 4)}"
              f" {f_rate_list[to_currency]['country']} {f_rate_list[to_currency]['currency']}.")

    # 4. Update exchange rates
    elif f_menu_choice == 4:
        exchange_menu(rate_list)

    # 5. Quit
    elif f_menu_choice == 5:
        print()
        print("Thank you for using the Conversion Utility.")
        input("Press <enter> to quit.")
        quit()


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
                       'Exit')

# intro
print("This program will help you convert currency")
print("")  # extra blank line

# Print rates
print_rates(rate_list)

# Current exchange fee as percentage
print("Exchange fee: " + "{:.2%}".format(conversion_fee))
print()

while True:
    print("- - - - - Conversion Utility - - - - -")
    print()
    display_menu(main_menu_tuple)
    # get input from user

    menu_response = get_menu_response(main_menu_tuple)

    main_action(menu_response, conversion_fee, rate_list)

    print()

    # cur_name = input("Tell me the name of the currency you have for exchange: ")
    # cur_amount = input("Enter the amount of " + cur_name + " you want to exchange: ")
    # cur_new_name = input("Tell me the name of the currency you want to convert to: ")
    # cur_exchange_rate = input("Enter the exchange rate from " + cur_name + " to " + cur_new_name + " : ")
    #
    # # calculate the conversion
    # cur_new_amount = float(cur_amount) / float(cur_exchange_rate)
    # cur_new_amount = round(cur_new_amount, 2)  # round to 2 digits

    # # print the results
    # print("")  # extra blank line
    # print("You can exchange", cur_amount, cur_name, "to", cur_new_amount, cur_new_name)
