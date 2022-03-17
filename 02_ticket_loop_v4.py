""" Noticed the count is actually incorrect. In the previous version
the program was counting the xxx as a sold seat
Also, further improved the emphasis - drawing the user's attention when
there is only one available seat left
"""

# Initialise loop so that it runs at least once
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
    name = input("what's your name? "). title()
    if name != "Xxx":
        count += 1 # Don't want to include escape code in the count

if count < Max_tickets:
    print(f"\nYou have sold {count} tickets\nThere are still "
          f"{Max_tickets - count} available ")
else:
    print("\nYou have sold all the available tickets")
