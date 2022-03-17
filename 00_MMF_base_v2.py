"""Added 01_name_not_blank_v3 to original v1 of this base code
"""

# import statement

# Functions go here

# Check that the ticket name is not blank
def not_blank(question):
    while True:
        response = input(question)
        if not response.isalpha(): # Ensures input contains at least 1 letter
            print("You can't leave this blank...") # Error if not
        else:
            return response


# ************ Main Routine ************

# Set up dictionaries / list need to hold data

# Ask user if they have used the program before and
# show instructions if necessary

# Loop to get ticket details

    # Get name (can't be blank)
    name = not_blank("What's your name: ", )

    # get age (between 12 to 130)

    # Calculate ticket price)

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method ( an apply surcharge if necessary)

# calculate total sales and profit

# Output data to text file

