"""Moved  the check of sales against maximum tickets into it's own function
added lists to hold ticket holder's name and the price paid for their ticket
added a dictionary to get data from these 2 new lists
added code to append name and ticket price to the new lists (line 137 and 138)
added the import re and import pandas libraries (installing pandas package if
necessary)
added the print statement for ticket profit on line 151
Modified the 'else' statements under 'if MAX_TICKETS - ticket_count > 1:'
(previously occupied lines 158-160) to improve flow and readability
added the print details (movie_frame: bottom 3 lines) which uses the pandas
library to create a printable DataFrame based on the dictionary
"""
# import statement
import re
import pandas # Might need to install pandas if library does not already exist


# Functions go here


# Calculate the ticket price (based on given age)
def calculate_ticket_price(ticket_age):...

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

