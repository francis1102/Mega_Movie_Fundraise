"""This component ask for a Yes/No response and keep asking until a valid
response is provided.
"""

error_message = "Please answer 'Y' or 'N'"
valid_responses = ["y", "yes", "no", "No"]
response = input("Do you want snacks? ").lower()
while response not in valid_responses:
    print(error_message)
    response = input("Do you want snacks? ").lower()

if response == "n" or response == "no":
    print("Valid_answer. You don't want snacks")
else:
    print("Valid_answer. You do want snacks")


