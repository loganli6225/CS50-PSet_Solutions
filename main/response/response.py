from validator_collection import checkers

input_email = input("What's your email address? ")
if checkers.is_email(input_email):
    print("Valid")
else:
    print("Invalid")
