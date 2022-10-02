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
            for row in reader:
                f_rate_dict[row['COUNTRY']] = {'currency': row['CURRENCY'], 'rate': row['RATE']}
        print(f_rate_dict)
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


# Main

# Initialize rate dictionary
rate_dict = dict()

# Load rates from file
rate_dict = load_rates(RATE_FILE)

# intro
print("This program will help you convert currency")
print("")  # extra blank line

# get input from user
cur_name = input("Tell me the name of the currency you have for exchange: ")
cur_amount = input("Enter the amount of " + cur_name + " you want to exchange: ")
cur_new_name = input("Tell me the name of the currency you want to convert to: ")
cur_exch_rate = input("Enter the exchange rate from " + cur_name + " to " + cur_new_name + " : ")

# calculate the conversion
cur_new_amount = float(cur_amount) / float(cur_exch_rate)
cur_new_amount = round(cur_new_amount,2) # round to 2 digits 

# print the results
print("") # extra blank line
print("You can exchange",cur_amount,cur_name,"to",cur_new_amount,cur_new_name)
