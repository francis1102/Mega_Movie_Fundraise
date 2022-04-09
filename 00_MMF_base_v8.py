"""Added 06_String_validator_v6 to 00_MMF_base_v7

"""
# import statement
import re
import pandas # Might need to install pandas if library does not a


# Functions go here
# This function splits snacks into quantify and snack name
# It has to be called before the snack (name) can be evaluated against the
# valid_snacks list
def split_order(choice):
    # Regular expression to test and find out if an item starts with an number
    number_regex = "^[1-9]"

    # if item has a number, separate the item into two: number and item
    if re.match(number_regex, choice):
        quantity_required = int(choice[0])
        snack_name = choice[1:]

    # if item has no number, assume number required is 1
    else:
        quantity_required = 1
        snack_name = choice

    # Need to remove white space from around snack
    snack_name = snack_name.strip()
    return quantity_required, snack_name

# Function takes the question and the list of valid choice as parameters
def get_choice(choice, valid_choices):
    choice_error = "Sorry that is not a valid choice"
    for list_item in valid_choices:
        if choice in list_item:
            choice = list_item[0].title()
            return choice
    print(choice_error)




# Calculate the ticket price (based on given age)
def calculate_ticket_price(ticket_age):
    # Ages - anything over standard_age must qualify for retired price
    child_age = range(12, 16)
    standard_age = range(16, 65)

    child_price = 7.5
    standard_price = 10.5
    retired_price = 6.5

    if ticket_age in child_age:
        price = child_price
    elif ticket_age in standard_age:
        price = retired_price
    else:
        price = retired_price

    return price


# check for valid integer (eg for age)
def number_checker(question):...


# Check that the ticket name is not blank
def not_blank(question):...


def check_max_tickets(maximum,sold):
    if maximum - sold > 1:
        print(f"\nthere are {maximum - sold} tickets left")
    else:
        # Warns user there is only one seat left
        print(f"\n**** There are ONLY one ticket left! ****")


def check_valid_tickets(maximum,sold):
    age = number_checker("Please enter {name}'s age: ")
    if age < minimum:
        print("Sorry, {name} is to you for this movie")
        return None
    else:
        while not age <= maximum: # age must be between 12 and 110
            age = number_checker(f"\nAt {age} {name} s very old. "
                                 "Please re-enter {name}'s age: ")
            return age
# ******** Main routine ********

# Set up dictionaries / lists to hold data
all_names = []
all_tickets = []


# Data frame dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets
}

MINIMUM_AGE = 12
MAXIMUM_AGE = 110
MAX_TICKETS = 5
TICKET_COST_PRICE = 5.00
name = ""
ticket_count = 0
profit = 0



# Set up dictionaries / list need to hold data

# Ask user if they have used the program before and
# show instructions if necessary

# Loop to get ticket details
# Initialize loop so that it runs at least once

while name != "Xxx" and ticket_count < MAX_TICKETS:
    # check to ensure there are still tickets left
    check_max_tickets(MAX_TICKETS, ticket_count)

    # get details
    # get name
    name = not_blank("Enter ticket-holder's name: ") # Name can't be blank
    if name = "Xxx":
        break
    else:
        # check for a valid age and then calculate ticket price
        age = check_valid_age(MINIMUM_AGE, MAXIMUM_AGE)
        if not age:
            continue # Restarts the get ticket loop
        else:
            ticket_count += 1 # Don't want escape code in the ticket_count

        # Calculate ticket price
        ticket_price = calculate_ticket_price(age)
        print(f"For {name} the price is ${ticket_price:,.2f} ")
        profit += (ticket_price - TICKET_COST_PRICE)

        # Add name and ticket price to lists
        all_names.append(name)
        all_tickets.append(ticket_price)

        # Get snacks

        # Get payment method (and work out surcharge as necessary)

    # End of ticket/snacks/payment loop


if ticket_count < MAX_TICKETS:
    if ticket_count > 1: # Making ure it reads OK when only one ticket sold
        print(f"\n{ticket_count} tickets have now been sold")
    else:
        print("1 ticket now has been sold")
    if MAX_TICKETS - ticket_count > 1:
        print(f"{MAX_TICKETS - ticket_count} tickets are still available\n")
    else:
        print("1 tickets are still available\n") # Making sure it reads OK when
        # only one ticket left

else:
    print("\n!!!!!!! All available tickets now has been sold !!!!!!!")
    print("*" * 60)

# Print details
movie_frame = pandas.DATAFrame(movie_data_dict)
print(movie_frame)
print(f"ticket profit is ${profit:.2f}")


# Loop to ask for snacks


    # get age (between 12 to 119)

    # Calculate ticket price)

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method ( an apply surcharge if necessary)

# calculate total sales and profit

# Output data to text file

