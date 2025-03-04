import re

def validate_email(email):
    if re.search(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        print("Email is valid")
        return email
    else:
        print("Email is invalid")
        return False

# Test cases
print(validate_email("harshal@gmail"))
validate_email("kjgfuwef.hfviuf-n")
