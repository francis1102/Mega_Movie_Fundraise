"""Added 04_calculate_ticket_price_v4
Also includes total profit calculation in main routine.
Have change the variable 'count' to 'ticket_count' and made the formatting
and language in the print statements easier to understand

"""
# import statement

# Functions go here
def calculate_ticket_price(age):
    # Ages - anything over standard_age must qualify for retired price
    child_age = range(12, 16)
    standard_age = range(16, 65)

    child_price = 7.5
    standard_price = 10.5
    retired_price = 6.5

    if age in child_age:
        price = child_price
    elif age in standard_age:
        price = standard_price
    else:
        price = retired_price

    return price


# Calculate the ticket price (based on given age)
# Check that the ticket name is not blank
def not_blank(question):
    while True:
        response = input(question).title()
        if not response.isalpha(): # Ensures input contains at least 1 letter
            print("You can't leave this blank...")  # Error if not
        else:
            return response


# check for valid integer (eg for age)
def number_checker(question):
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number 
        except ValueError:
            print("\nPlease enter an integer (ie a whole number "
                  "with no decimals")
# ************ Main Routine ************

# Set up dictionaries / list need to hold data

# Ask user if they have used the program before and
# show instructions if necessary

# Loop to get ticket details
name = ""
ticket_seat = 0
profit = 0
Max_tickets = 5
TICKET_COST_PRICE = 5.00


while name != "Xxx" and ticket_count < Max_tickets:
    if Max_tickets - ticket_count > 1:
        print(f"\nYou have {Max_tickets - ticket_count} ticket left")
    else:
        # Warns user there is only one seat eft
        print(f"\n**** You have ONLY ONE seat left! ****")
    # Get details
    name = not_blank("what's your name? ")
    if name != "Xxx":
        break
    else:
        MINIMUM_AGE = 12
        MAXIMUM_AGE = 110
        age = number_checker("Please enter the age of the ticket-holder: ")
        if age < MINIMUM_AGE:
            print("Sorry, you are too young for this movie")
        else:
            while not age <= MAXIMUM_AGE:  # age must be between 12 and 110
                    age = number_checker(f"\nAt {age} {name} is very old, "
                                         f"Please re-enter {name}'s age: ")
                ticket_count += 1  # Don't want to include escape code in the ticket_count

                # Calculate ticket price)
                ticket_price = calculate_ticket_price(age)
                print(f"For {name} the price is ${ticket_price:,.2f}")
                profit += (ticket_price - TICKET_COST_PRICE)

# calculate total sales and profit
if ticket_count < Max_tickets:
    if ticket_count > 1: # Making sure it reads OK when only one ticket sold
        print (f"\n{ticket_count} ticket have now been sold")
    else:
        print("1 ticket has now been sold")
    if Max_tickets - ticket_count > 1:
        print(f"{Max_tickets - ticket_count} tickets are still available\n")
    else:
        print("1 ticket is  available\n") # Making sure it reads OK when
        # only one ticket left

else:
    print("\n!!!!!!!! ALl the available tickets have now been sold !!!!!!!!")
    print("*"* 60)

print(f"Ticket profit is $ {profit:.2f}")


    # get age (between 12 to 119)

    # Calculate ticket price)

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method ( an apply surcharge if necessary)



# Output data to text file

