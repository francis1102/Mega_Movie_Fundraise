""" This version includes a print statement at the start, saying how many
tickets are still available for sold
"""

# Initialise loop so that it runs at least once
name = ""
count = 0
Max_tickets = 5

while name != "Xxx" and count != 5:
    print(f"\nYou have {Max_tickets - count} seats left")
    # Get details
    name = input("what's your name? "). title()
    count += 1

if count < Max_tickets:
    print(f"\nYou have sold {count} tickets\nThere are still "
          f"{Max_tickets - count} available ")
else:
    print("\nYou have sold all the available tickets")
