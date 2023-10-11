import validators

# Get user's input
email = input("What's your email? ").strip().lower()

# Validate user's input
validate = validators.email(email)

if validate:
    print("Valid")
else:
    print("Invalid")
