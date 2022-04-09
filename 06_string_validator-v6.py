"""Based on 06_String_Validator_v5,
Takes the snack ordering code out of the main routine and puts it inside its
own funtions
"""

import re


# This function splits snacks into quantity and snack name
# It has to be called before the snack (name) can be evaluated against the
# valid_snack list
def split_order(choice):
    # Regular expression to test and find oit if an item starts with a number
    number_regex = "^[1-9]"

    # if item has a number, separate the item into two: number and item
    if re.match(number_regex, choice):
        quantity_required = int(choice[0])
        snack_name = choice [1:]

    # If item has no number, assume number required is 1
    else:
        quantity_required = 1
        snack_name = choice

    # Need to remove white space from around snack
    snack_name = snack_name.strip()
    return quantity_required, snack_name


# Function takes the question and list of valid choices as parameters
def get_choice(choice, valid_choices):
    choice_error = "Sorry, that is not valid choice"
    for list_item in valid_choices:
        if choice in list_item:
            choice = list_item[0].title()
            return choice
    print(choice_error)


# Main routine
ask_for_snack = "what snacks do you want - 'x' to stop ordering: "

# Valid snacks holds list of all snacks, Each item s itself  list with all
# The acceptable input option for each snacks - full names, initials and
# abbreviations, as well as a reference number
valid_snacks = [["popcorn", "p", "corn", "1"], ["m&ms", "mms", "m", "2"],
                    ["pita chips", "chips", "pc", "pita", "c", "3"],
                    ["water", "w", "4"], ["x", "exit," "(5"],
                ["x", "exit", "(6"]]

# Valid option for yes/no question
valid_yes_no = [["y", "yes"], ["n", "no"]]

# The snack_order list records the complete order for a single user
snack_order = []
# Maximum number of any snack item which can be ordered
max_number_of_snacks = 4
# Assumption that every user will want to order snacks
getting_snacks = True
while getting_snacks:
    # Firstly, find out whether the user wants to order snacks
    snack_required = ""
    while snacks_required != "N" and snack_required != "Y":
        # Response is passed to the generic string checking function with the
        # The list of valid yes/no responses as parameters
        checking_snacks = input("Do you want snacks? (Y/N): ").lower()
        snack_required = get_choice(checking_snacks, valid_yes_no)

    if snacks_required == "N": # but if they don't want any snacks
        getting_snacks = False # break the while loop
        break

    else:
        # Otherwise, for each snack, the generic string checker is called with
        # the 'ask_for_snacks' question and the list of valid snacks as
        # parameters
        option = ""
        while option != "X":
            snack = input("What snack do you want - or 'x' to stop "
                          "ordering: ").lower()
            snacks = split_order(snack)
            quantity = snack[0]
            if quantity > max_number_of_snacks:
                snack = None
                print("Sorry, the maximum number you can order is 4")
            else:
                snack = snack[1]
                option = get_choice(snack, valid_snacks)
                if option == "X":
                    getting_snacks = False

                elif option is not None: # Filters out invalid choice
                    snack_order.append(quantity, option)

# After the loop is broken, check for an empty list
if len(snack_order) > 0: # If there is something in the list, print each item
    print("\nThis is a summary of your order:")
    for item in snack_order:
        print(f"\t{item[0]} {item[1]}")
else: # Otherwise, print this
    print("No snacks were ordered")



