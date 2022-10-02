# John Logiudice
# WA # 6 - Write a program for currency exchange / conversion.

import csv  # csv Library to load and save exchange rate data
import math

# Constant for rate file name
RATE_FILE = 'conversion_rates.csv'


# Check if string can be converted to float
def is_float(f_string):
    try:
        float(f_string.strip())
        return True
    except ValueError:
        return False


# Load rates from CSV file
def load_rates(rate_file):
    f_rate_dict = dict()
    # Attempt to open and read data file
    try:
        with open(rate_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            i = 0  # counter
            for row in reader:
                i += 1
                f_rate_dict[row['COUNTRY']] = {'order': i, 'currency': row['CURRENCY'], 'rate': row['RATE']}

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

    return f_rate_dict


# Print current rates
def print_rates(f_rate_dict):

    # List is printed in two columns
    country_list = list(f_rate_dict)
    list_len = len(country_list)

    # To get the number of entries to print on the left side divide
    # list length in half but always have the greater number of
    # entries on the left side
    # math.ceil returns an integer rounded up
    half_list_len = math.ceil(list_len / 2)

    # Heading
    print('#   ' + 'Currency Name' + " "*2 + 'Country' + " "*11 + 'Rate', end='')
    print(" "*10, end='')
    print('#   ' + 'Currency Name' + " "*2 + 'Country' + " "*11 + 'Rate')
    print('-'*43, end='')
    print(" "*8, end='')
    print('-'*43)

    for i in range(0, half_list_len):
        # Print left side list
        country1 = country_list[i]
        order = str(f_rate_dict[country1]['order']) + ". "
        currency1 = f_rate_dict[country1]['currency']
        rate1 = f_rate_dict[country1]['rate']
        print(order, end='')
        print(" "*(4-len(order)), end='')
        print(currency1, end='')
        print(" "*(15-len(currency1)), end='')
        print(country1, end='')
        print(" "*(18-len(country1)), end='')
        print(rate1, end='')
        # If right list shorter than left list, avoid error
        if (i + half_list_len) < list_len:
            # Print right side list
            country2 = country_list[i + half_list_len]
            order2 = str(f_rate_dict[country2]['order']) + ". "
            currency2 = f_rate_dict[country2]['currency']
            rate2 = f_rate_dict[country2]['rate']
            print(" "*(14-len(rate1)), end='')
            print(order2, end='')
            print(" "*(4-len(order2)), end='')
            print(currency2, end='')
            print(" "*(15-len(currency2)), end='')
            print(country2, end='')
            print(" "*(18-len(country2)), end='')
            print(rate2)
        else:
            # Filler for no right entry
            print()
    print()


# Print main menu
def main_menu(f_menu_tuple):
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


# Get and validate new conversion fee
def get_new_fee(f_conversion_fee):
    # loop until valid response or quit
    while True:
        response = input("Please enter the new fee as a percent: ").strip()
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


# Perform main menu action
def main_action(f_menu_choice, f_conv_fee):

    # 1. Show exchange rates
    if f_menu_choice == 1:
        # Print rates
        print()
        print_rates(rate_dict)

    # 2. Set exchange fee
    elif f_menu_choice == 2:
        print()
        print("Exchange fee is a percentage of final conversion amount.")
        print("Current exchange fee: " + "{:.2%}".format(f_conv_fee))
        f_conv_fee = get_new_fee(f_conv_fee)
        print()
        print("The new conversion fee is " + "{:.2%}".format(f_conv_fee))

    # 3. Convert a currency


    # 4. Update exchange rates


    # 5. Quit


# Main
# Set default conversion fee
conversion_fee = 0.01

# Load rates into dictionary from file
rate_dict = load_rates(RATE_FILE)

# Menu options
main_menu_tuple = ('Show exchange rates', 'Set exchange fee', 'Convert a currency',
                   'Update exchange rates', 'Quit')

# intro
print("This program will help you convert currency")
print("")  # extra blank line

# Print rates
print_rates(rate_dict)

# Current exchange fee as percentage
print("Exchange fee: " + "{:.2%}".format(conversion_fee))
print()

while True:
    main_menu(main_menu_tuple)
    # get input from user

    menu_response = get_menu_response(main_menu_tuple)

    main_action(menu_response, conversion_fee)

    print()

    cur_name = input("Tell me the name of the currency you have for exchange: ")
    cur_amount = input("Enter the amount of " + cur_name + " you want to exchange: ")
    cur_new_name = input("Tell me the name of the currency you want to convert to: ")
    cur_exchange_rate = input("Enter the exchange rate from " + cur_name + " to " + cur_new_name + " : ")

    # calculate the conversion
    cur_new_amount = float(cur_amount) / float(cur_exchange_rate)
    cur_new_amount = round(cur_new_amount, 2)  # round to 2 digits

    # print the results
    print("")  # extra blank line
    print("You can exchange", cur_amount, cur_name, "to", cur_new_amount, cur_new_name)
