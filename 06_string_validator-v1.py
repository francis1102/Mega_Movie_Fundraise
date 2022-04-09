"""Based on 05_Yes_No_v3, This program uses test list of snacks 'valid_snacks'
Each item in valid snacks is a list with the valid options for each snack.
These are: full name, code 1-4, and some possible abbreviation.
"""


def get_snacks():
    snacks_choice_error = "Sorry, that is not a valid choice"
    valid_snacks = [["popcorn", "p", "corn", "1"], ["m&ms", "mms", "m", "2"],
                    ["pita chips", "chips", "pc", "pita", "c", "3"],
                    ["water", "w", "4"]]
    snack_choice = input("Snack: ").lower()
    for snack in valid_snacks:
        if snack_choice in snack:
            snack_choice = snack[0].title()
            return snack_choice

        print(snacks_choice_error)
        return get_snacks()


# Main routine
# temporary input statement - during development
for test in range(6):
    print(f"You want {get_snacks()}")


