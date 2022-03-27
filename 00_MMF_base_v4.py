"""Added 03_age_validator_v4
"""
# import statement

# Functions go here

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
# ************ Main Routine ************

# Set up dictionaries / list need to hold data

# Ask user if they have used the program before and
# show instructions if necessary

# Loop to get ticket details
name = ""
count = 0
Max_tickets = 5

while name != "Xxx" and count < Max_tickets:
    if Max_tickets - count > 1:
        print(f"\nYou have {Max_tickets - count} seats left")
    else:
        # Warns user there is only one seat eft
        print(f"\n****You have ONLY ONE seat left! ****")
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
                age = number_checker("\nPLease enter an integer between 12 and 110: ")
                count += 1  # Don't want to include escape code in the count

if count < Max_tickets:
    print(f"\nYou have sold {count} tickets\nThere are still "
                  f"{Max_tickets - count} available ")
else:
    print("\nYou have sold all the available tickets")


    # get age (between 12 to 119)

    # Calculate ticket price)

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method ( an apply surcharge if necessary)

# calculate total sales and profit

# Output data to text file

