""" Integer checking function - loops until a valid number is entered
This version uses 'isinstance()' to validate the integer and cuts down on
the number of parameters required in the function by incorporating the valid
age range into a loop in the main routine
"""

def number_checker(text):
    valid = False
    while not valid:
        try:
            number_to_check = int(input(text))
            if insinstance(number_to_check, int):
                valid = True
                return number_to_check
        except ValueError:
            print("\nPlease enter an integer (ie a whole number "
                  "with no decimals)")


# Main routine
# Check for a valid age - must be between 12 and 110
age = number_checker("Please enter the age of tge ticket-holder: ")
while not 12 <= age <= 110:
    age = number_to_checker("\nPlease enter an integer between 12 and 110: ")
print(f"Age = {age}")




