# John Logiudice
# WA # 6 - Write a program for currency exchange / conversion.

import csv  # csv Library to load and save exchange rate data

# Constant for rate file name
RATE_FILE = 'conversion_rates.csv'


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
    half_list_len = (list_len // 2) + 1
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
    print()
    print()



# Main

# Set default conversion fee
conversion_fee = 0.01

# Load rates into dictionary from file
rate_dict = load_rates(RATE_FILE)

# intro
print("This program will help you convert currency")
print("")  # extra blank line

# Print rates
print_rates(rate_dict)

# get input from user
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
