""" 3rd iteration of the integer checking function
Simplified try/except and created AGE_RANGE as a constant
"""

def number_checker(question):
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print("\nPlease enter an integer (ie a whole number "
                  "with no decimals)")


# Main routine
# Check for a valid age - must be between 12 and 110
AGE_Range = range(12, 111)  # Between 12 and 110 inclusive
age = number_checker("Please enter the age of tge ticket-holder: ")
while age not in AGE_Range:  # age must be between 12 and 110
    age = number_checker("\nPlease enter an integer between 12 and 110: ")

print(f"Age = {age}")




